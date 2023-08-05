#  ---------------------------------------------------------------------------------
#  Copyright (c) 2023 DataRobot, Inc. and its affiliates. All rights reserved.
#  Last updated 2023.
#
#  DataRobot, Inc. Confidential.
#  This is proprietary source code of DataRobot, Inc. and its affiliates.
#
#  This file and its contents are subject to DataRobot Tool and Utility Agreement.
#  For details, see
#  https://www.datarobot.com/wp-content/uploads/2021/07/DataRobot-Tool-and-Utility-Agreement.pdf.
#  ---------------------------------------------------------------------------------
import logging
import os
import time
from pathlib import Path

import pandas as pd

MAX_RAW_ROWS = 10000
MODEL_PATH = Path(os.environ["AZUREML_MODEL_DIR"]) / os.environ["DATAROBOT_MODEL_FILENAME"]


def init():
    set_java_home()  # noqa: F821

    # TODO: [AGENT-4189] to work around jpype issues, we can't start the JVM until
    # we are in the worker process (after the fork). For now just do some simple
    # sanity checks.
    if not MODEL_PATH.exists():
        raise RuntimeError(f"Model JAR is not present: {MODEL_PATH}")


def run(mini_batch):
    start_time = time.monotonic_ns()
    model, model_id = load_model(MODEL_PATH)  # noqa: F821
    # AGENT-4338: calculate feature_types (e.g. FeatureDescriptors) for the model to support
    # stats agg
    mlops_sdk = get_mlops(model_id=model_id)  # noqa: F821

    # TODO: not sure how to pass params at runtime so just use the defaults for now.
    params = GenericModelParams()  # noqa: F821
    return make_prediction(model, mini_batch, params, mlops_sdk, start_time)


def make_prediction(model, scoring_batches, params, mlops_sdk, start_time) -> pd.DataFrame:
    incoming = []
    results = []
    for iteration, file_path in enumerate(scoring_batches, start=1):
        try:
            df = pd.read_csv(file_path, dtype=model.features)
        except Exception:
            logging.exception("#%s: error while loading inference data: %s", iteration, file_path)
            continue

        try:
            logging.info("Scoring batch #%s", iteration)
            predictions: pd.DataFrame = model.predict(df, **params.dict())
        except Exception:
            # Log the error but continue so we can correctly support the `error_threshold`
            # the user has configured. The AzureML platform does this by monitoring the
            # the gap between mini-batch input count and returns. 'Batch inferencing' scenario
            # should return a list, dataframe, or tuple with the successful items to try to meet
            # this threshold.
            logging.exception("#%s: error while scoring: %s", iteration, df)
            predictions = pd.DataFrame()
        if predictions.empty:
            logging.warning("Empty results, batch #%s", iteration)
            # TODO: add logic to fillna prediction data so it will line up with feature data and
            # we can at least send that but for now just skip the batch entirely.
            continue

        # Only if we've made it this far, can we add the mini-batch to our combined results
        incoming.append(df)
        results.append(predictions)
    combined_predictions = pd.concat(results) if results else pd.DataFrame()
    combined_scoring_data = pd.concat(incoming) if incoming else pd.DataFrame()

    report_service_health_via_tracking_agent(  # noqa: F821
        mlops_sdk, start_time, combined_predictions
    )
    report_predictions_data_via_tracking_agent(  # noqa: F821
        mlops_sdk,
        model,
        combined_predictions,
        combined_scoring_data,
        params,
        # AGENT-4338: Uncomment when MLOps init is done
        # max_unaggregated_rows=MAX_RAW_ROWS,
    )
    return combined_predictions

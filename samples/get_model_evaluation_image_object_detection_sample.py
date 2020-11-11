# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_get_model_evaluation_image_object_detection_sample]
from google.cloud import aiplatform


def run_sample():
    # TODO(dev): replace these variables to run the code
    project = "YOUR-PROJECT-ID"
    model_id = "YOUR-MODEL-ID"
    evaluation_id = "YOUR-EVALUATION-ID"
    get_model_evaluation_image_object_detection_sample(project, model_id, evaluation_id)


def get_model_evaluation_image_object_detection_sample(
    project: str, model_id: str, evaluation_id: str, location: str = "us-central1"
):
    client_options = {"api_endpoint": "us-central1-aiplatform.googleapis.com"}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.ModelServiceClient(client_options=client_options)
    name = client.model_evaluation_path(
        project=project, location=location, model=model_id, evaluation=evaluation_id
    )
    response = client.get_model_evaluation(name=name)
    print("response:", response)


# [END aiplatform_get_model_evaluation_image_object_detection_sample]

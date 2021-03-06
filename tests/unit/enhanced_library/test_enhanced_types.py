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
from __future__ import absolute_import

from google.cloud.aiplatform.v1beta1.schema.trainingjob import definition

ModelType = definition.AutoMlImageClassificationInputs().ModelType
test_training_input = definition.AutoMlImageClassificationInputs(
    multi_label=True,
    model_type=ModelType.CLOUD,
    budget_milli_node_hours=8000,
    disable_early_stopping=False,
)


def test_exposes_to_value_method():
    assert hasattr(test_training_input, "to_value")


def test_exposes_from_value_method():
    assert hasattr(test_training_input, "from_value")


def test_exposes_from_map_method():
    assert hasattr(test_training_input, "from_map")

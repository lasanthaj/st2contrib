# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from lib.icsp import ICSPBaseActions


class GetBuildPlans(ICSPBaseActions):
    def run(self, plan_names, connection_details):
        if connection_details:
            self.setConnection(connection_details)
        self.getSessionID()

        endpoint = "/rest/os-deployment-build-plans"
        results = self.icspGET(endpoint)
        plans = []
        for plan in results["members"]:
            if plan_names:
                for name in plan_names:
                    if name.lower() == str(plan["name"]).lower():
                        uri = plan["uri"].split("/")[-1]
                        plans.append({"name": plan["name"], "uri": uri})
            else:
                uri = plan["uri"].split("/")[-1]
                plans.append({"name": plan["name"], "uri": uri})

        return {"plans": plans}

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pyramid.httpexceptions import HTTPMovedPermanently


def redirect_view_factory(target, redirect=HTTPMovedPermanently):
    def redirect_view(request):
        return redirect(target.format(_request=request, **request.matchdict))
    return redirect_view


def add_redirect(config, source, target, **kw):
    route_name = "warehouse.redirects." + source

    config.add_route(route_name, source)
    config.add_view(redirect_view_factory(target, **kw), route_name=route_name)


def includeme(config):
    config.add_directive("add_redirect", add_redirect, action_wrap=False)

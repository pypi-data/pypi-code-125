import pdb

from typing import List, Union

from mitmproxy.http import Request as MitmproxyRequest

from stoobly_agent.app.settings.constants import firewall_action, intercept_mode
from stoobly_agent.app.settings.filter_rule import FilterRule
from stoobly_agent.app.settings.firewall_rule import FirewallRule
from stoobly_agent.app.settings import Settings
from stoobly_agent.config.constants import custom_headers, mode, request_origin
from stoobly_agent.lib.api.keys.project_key import InvalidProjectKey, ProjectKey

class InterceptSettings:

  def __init__(self, settings: Settings, request: MitmproxyRequest = None):
    self.__settings = settings
    self.__request = request
    self.__headers: MitmproxyRequest.headers = None

    if request:
      self.__headers = request.headers

    project_id = None

    try: 
      project_key = ProjectKey(self.project_key)
      project_id = project_key.id
    except InvalidProjectKey:
      pass

    # If no valid project key is provided, use default settings,
    # Otherwise, set settings for the project
    self.__data_rules = self.__settings.proxy.data.data_rules(project_id)
    self.__filter_rules = self.__settings.proxy.filter.filter_rules(project_id)
    self.__firewall_rules = self.__settings.proxy.firewall.firewall_rules(project_id)
    self.__intercept_settings = self.__settings.proxy.intercept 

  @property
  def settings(self):
    return self.__settings

  @property
  def active(self):
    if self.__intercept_settings.active:
      return True
    
    return self.__headers and custom_headers.PROXY_MODE in self.__headers

  @property
  def mode(self):
    if self.__headers:
      '''
      access_control_header = self.__headers.get('Access-Control-Request-Headers')
      do_proxy_header = custom_headers.DO_PROXY

      if access_control_header and do_proxy_header.lower() in access_control_header:
          return mode.NONE

      if do_proxy_header in self.__headers:
          return mode.NONE
      '''

      if custom_headers.PROXY_MODE in self.__headers:
          return self.__headers[custom_headers.PROXY_MODE]

    return self.__intercept_settings.mode

  @property
  def project_key(self):
    if self.__headers and custom_headers.PROJECT_KEY in self.__headers:
        return self.__headers[custom_headers.PROJECT_KEY]

    return self.__settings.proxy.intercept.project_key

  @property
  def response_mode(self):
    if custom_headers.RESPONSE_PROXY_MODE in self.__headers:
      return self.__headers[custom_headers.RESPONSE_PROXY_MODE]

    return self.mode

  @property
  def scenario_key(self):
    if self.__headers and custom_headers.SCENARIO_KEY in self.__headers:
        return self.__headers[custom_headers.SCENARIO_KEY]

    return self.__data_rules.scenario_key

  @scenario_key.setter
  def scenario_key(self, v):
    self.__data_rules.scenario_key = v

  @property
  def report_key(self) -> Union[str, None]:
    if self.__headers and custom_headers.REPORT_KEY in self.__headers:
      return self.__headers[custom_headers.REPORT_KEY]

  @property
  def policy(self):
    mode = self.mode
    if mode == intercept_mode.MOCK:
      if self.__headers and custom_headers.MOCK_POLICY in self.__headers:
        return self.__headers[custom_headers.MOCK_POLICY]

      return self.__data_rules.mock_policy
    elif mode == intercept_mode.RECORD:
      if self.__headers and custom_headers.RECORD_POLICY in self.__headers:
        return self.__headers[custom_headers.RECORD_POLICY]

      return self.__data_rules.record_policy
    elif mode == intercept_mode.TEST:
      return self.__data_rules.test_policy
    elif mode == intercept_mode.REPLAY:
      return self.__data_rules.replay_policy

  @property
  def exclude_rules(self) -> List[FirewallRule]:
    return list(filter(lambda rule: rule.action == firewall_action.EXCLUDE, self.__firewall_rules))

  @property
  def include_rules(self) -> List[FirewallRule]:
    return list(filter(lambda rule: rule.action == firewall_action.INCLUDE, self.__firewall_rules))

  @property
  def redact_rules(self) -> List[FilterRule]:
    return self.__select_filter_rules()

  @property
  def ignore_rules(self) -> List[FilterRule]:
    return self.__select_filter_rules()

  @property
  def rewrite_rules(self) -> List[FilterRule]:
    return self.__select_filter_rules()

  @property
  def upstream_url(self):
    if self.__headers and custom_headers.SERVICE_URL in self.__headers:
      return self.__headers[custom_headers.SERVICE_URL]

    settings_upstream_url = self.__intercept_settings.upstream_url
    if settings_upstream_url and len(settings_upstream_url) > 0:
      return self.__intercept_settings.upstream_url

    if self.__request:
      return f"{self.__request.scheme}://{self.__request.host}:{self.__request.port}"
  
  @property
  def test_strategy(self):
    if self.__headers and custom_headers.TEST_STRATEGY in self.__headers:
      return self.__headers[custom_headers.TEST_STRATEGY]

    return self.__data_rules.test_strategy

  @property
  def request_origin(self):
    if self.__headers and custom_headers.REQUEST_ORIGIN in self.__headers:
      return self.__headers[custom_headers.REQUEST_ORIGIN]

    return request_origin.WEB

  def __select_filter_rules(self):
    rules = []

    # Filter only parameters matching active intercept mode
    for filter_rule in self.__filter_rules:
      parameter_rules = self.__select_parameter_rules(filter_rule)

      # If no parameters rules were found, then this filter rule is not applied
      if len(parameter_rules) == 0:
        continue

      # Build a new FilterRule object contain only parameter rules matching intercept mode
      filter_rule = FilterRule({
        'methods': filter_rule.methods,
        'pattern': filter_rule.pattern,
        'parameters_rules': [], # Has to be dict form, manually set it
      })
      filter_rule.parameter_rules = parameter_rules

      rules.append(filter_rule)

    return rules

  def __select_parameter_rules(self, filter_rule: FilterRule):
    return list(filter(
      lambda parameter: self.mode in parameter.modes and parameter.name, 
      filter_rule.parameter_rules or []
    ))
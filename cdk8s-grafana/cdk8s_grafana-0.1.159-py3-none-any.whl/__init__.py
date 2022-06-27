'''
## cdk8s-grafana

[![View on Construct Hub](https://constructs.dev/badge?package=cdk8s-grafana)](https://constructs.dev/packages/cdk8s-grafana)

cdk8s-grafana is a library that lets you easily define a Grafana service for
your kubernetes cluster along with associated dashboards and datasources, using
a high level API.

### Usage

To apply the resources generated by this construct, the Grafana operator must be
installed on your cluster. See
[https://operatorhub.io/operator/grafana-operator](https://operatorhub.io/operator/grafana-operator) for full installation
instructions.

The following will define a Grafana cluster connected to a Prometheus
datasource:

```typescript
import { Grafana } from 'cdk8s-grafana';

// inside your chart:
const grafana = new Grafana(this, 'my-grafana', {
  defaultDataSource: {
    name: 'Prometheus',
    type: 'prometheus',
    access: 'proxy',
    url: 'http://prometheus-service:9090',
  }
});
```

Basic aspects of a dashboard can be customized:

```typescript
const github = grafana.addDatasource('github', ...);
const dashboard = grafana.addDashboard('my-dashboard', {
  title: 'My Dashboard',
  refreshRate: Duration.seconds(10),
  timeRange: Duration.hours(6), // show metrics from now-6h to now
  plugins: [
    {
      name: 'grafana-piechart-panel',
      version: '1.3.6',
    }
  ],
});
```

Note: the kubernetes grafana operator only supports one Grafana instance per
namespace (see https://github.com/grafana-operator/grafana-operator/issues/174).
This may require specifying namespaces explicitly, e.g.:

```typescript
const devGrafana = new Grafana(this, 'my-grafana', {
  namespace: 'dev',
});
const prodGrafana = new Grafana(this, 'my-grafana', {
  namespace: 'prod',
});
```

The grafana operator must be installed in each namespace for the resources in
that namespace to be recognized.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more
information.

## License

This project is licensed under the Apache-2.0 License.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import cdk8s
import constructs


@jsii.enum(jsii_type="cdk8s-grafana.AccessType")
class AccessType(enum.Enum):
    '''Mode for accessing a data source.

    :see: https://grafana.com/docs/grafana/latest/administration/provisioning/#example-data-source-config-file
    '''

    PROXY = "PROXY"
    '''Access via proxy.'''
    DIRECT = "DIRECT"
    '''Access directly (via server or browser in UI).'''


class Dashboard(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-grafana.Dashboard",
):
    '''A Grafana dashboard.

    :see: https://grafana.com/docs/grafana/latest/http_api/dashboard/
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        title: builtins.str,
        data_source_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        folder: typing.Optional[builtins.str] = None,
        json_model: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        plugins: typing.Optional[typing.Sequence["GrafanaPlugin"]] = None,
        refresh_rate: typing.Optional[cdk8s.Duration] = None,
        time_range: typing.Optional[cdk8s.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param title: Title of the dashboard.
        :param data_source_variables: Specify a mapping from data source variables to data source names. This is only needed if you are importing an existing dashboard's JSON and it specifies variables within an "__inputs" field. Default: - no data source variables
        :param folder: Group dashboards into folders. Default: - default folder
        :param json_model: All other dashboard customizations.
        :param labels: Labels to apply to the kubernetes resource. When adding a dashboard to a Grafana instance using ``grafana.addDashboard``, labels provided to Grafana will be automatically applied. Otherwise, labels must be added manually. Default: - no labels
        :param namespace: Namespace to apply to the kubernetes resource. When adding a dashboard to a Grafana instance using ``grafana.addDashboard``, the namespace will be automatically inherited. Default: - undefined (will be assigned to the 'default' namespace)
        :param plugins: Specify plugins required by the dashboard.
        :param refresh_rate: Auto-refresh interval. Default: - 5 seconds
        :param time_range: Time range for the dashboard, e.g. last 6 hours, last 7 days, etc. Default: - 6 hours
        '''
        props = DashboardProps(
            title=title,
            data_source_variables=data_source_variables,
            folder=folder,
            json_model=json_model,
            labels=labels,
            namespace=namespace,
            plugins=plugins,
            refresh_rate=refresh_rate,
            time_range=time_range,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addPlugins")
    def add_plugins(self, *plugins: "GrafanaPlugin") -> None:
        '''Adds one or more plugins.

        :param plugins: -
        '''
        return typing.cast(None, jsii.invoke(self, "addPlugins", [*plugins]))


@jsii.data_type(
    jsii_type="cdk8s-grafana.DashboardProps",
    jsii_struct_bases=[],
    name_mapping={
        "title": "title",
        "data_source_variables": "dataSourceVariables",
        "folder": "folder",
        "json_model": "jsonModel",
        "labels": "labels",
        "namespace": "namespace",
        "plugins": "plugins",
        "refresh_rate": "refreshRate",
        "time_range": "timeRange",
    },
)
class DashboardProps:
    def __init__(
        self,
        *,
        title: builtins.str,
        data_source_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        folder: typing.Optional[builtins.str] = None,
        json_model: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        plugins: typing.Optional[typing.Sequence["GrafanaPlugin"]] = None,
        refresh_rate: typing.Optional[cdk8s.Duration] = None,
        time_range: typing.Optional[cdk8s.Duration] = None,
    ) -> None:
        '''
        :param title: Title of the dashboard.
        :param data_source_variables: Specify a mapping from data source variables to data source names. This is only needed if you are importing an existing dashboard's JSON and it specifies variables within an "__inputs" field. Default: - no data source variables
        :param folder: Group dashboards into folders. Default: - default folder
        :param json_model: All other dashboard customizations.
        :param labels: Labels to apply to the kubernetes resource. When adding a dashboard to a Grafana instance using ``grafana.addDashboard``, labels provided to Grafana will be automatically applied. Otherwise, labels must be added manually. Default: - no labels
        :param namespace: Namespace to apply to the kubernetes resource. When adding a dashboard to a Grafana instance using ``grafana.addDashboard``, the namespace will be automatically inherited. Default: - undefined (will be assigned to the 'default' namespace)
        :param plugins: Specify plugins required by the dashboard.
        :param refresh_rate: Auto-refresh interval. Default: - 5 seconds
        :param time_range: Time range for the dashboard, e.g. last 6 hours, last 7 days, etc. Default: - 6 hours
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "title": title,
        }
        if data_source_variables is not None:
            self._values["data_source_variables"] = data_source_variables
        if folder is not None:
            self._values["folder"] = folder
        if json_model is not None:
            self._values["json_model"] = json_model
        if labels is not None:
            self._values["labels"] = labels
        if namespace is not None:
            self._values["namespace"] = namespace
        if plugins is not None:
            self._values["plugins"] = plugins
        if refresh_rate is not None:
            self._values["refresh_rate"] = refresh_rate
        if time_range is not None:
            self._values["time_range"] = time_range

    @builtins.property
    def title(self) -> builtins.str:
        '''Title of the dashboard.'''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Specify a mapping from data source variables to data source names.

        This is only needed if you are importing an existing dashboard's JSON
        and it specifies variables within an "__inputs" field.

        :default: - no data source variables

        Example::

            { DS_PROMETHEUS: "my-prometheus-ds" }
        '''
        result = self._values.get("data_source_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def folder(self) -> typing.Optional[builtins.str]:
        '''Group dashboards into folders.

        :default: - default folder
        '''
        result = self._values.get("folder")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def json_model(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''All other dashboard customizations.

        :see: https://grafana.com/docs/grafana/latest/dashboards/json-model/
        '''
        result = self._values.get("json_model")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels to apply to the kubernetes resource.

        When adding a dashboard to a Grafana instance using ``grafana.addDashboard``,
        labels provided to Grafana will be automatically applied. Otherwise,
        labels must be added manually.

        :default: - no labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace to apply to the kubernetes resource.

        When adding a dashboard to a Grafana instance using ``grafana.addDashboard``,
        the namespace will be automatically inherited.

        :default: - undefined (will be assigned to the 'default' namespace)
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugins(self) -> typing.Optional[typing.List["GrafanaPlugin"]]:
        '''Specify plugins required by the dashboard.'''
        result = self._values.get("plugins")
        return typing.cast(typing.Optional[typing.List["GrafanaPlugin"]], result)

    @builtins.property
    def refresh_rate(self) -> typing.Optional[cdk8s.Duration]:
        '''Auto-refresh interval.

        :default: - 5 seconds
        '''
        result = self._values.get("refresh_rate")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    @builtins.property
    def time_range(self) -> typing.Optional[cdk8s.Duration]:
        '''Time range for the dashboard, e.g. last 6 hours, last 7 days, etc.

        :default: - 6 hours
        '''
        result = self._values.get("time_range")
        return typing.cast(typing.Optional[cdk8s.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataSource(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-grafana.DataSource",
):
    '''A Grafana data source.

    :see: https://grafana.com/docs/grafana/latest/administration/provisioning/#example-data-source-config-file
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        access: AccessType,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param access: Access type of the data source.
        :param name: Name of the data source.
        :param type: Type of the data source.
        :param description: Description of the data source. Default: - no description
        :param labels: Labels to apply to the kubernetes resource. When adding a data source to a Grafana instance using ``grafana.addDataSource``, labels provided to Grafana will be automatically applied. Otherwise, labels must be added manually. Default: - no labels
        :param namespace: Namespace to apply to the kubernetes resource. When adding a data source to a Grafana instance using ``grafana.addDataSource``, the namespace will be automatically inherited. Default: - undefined (will be assigned to the 'default' namespace)
        :param url: URL of the data source. Most resources besides the 'testdata' data source type require this field in order to retrieve data. Default: - default url for data source type
        '''
        props = DataSourceProps(
            access=access,
            name=name,
            type=type,
            description=description,
            labels=labels,
            namespace=namespace,
            url=url,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Name of the data source.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))


@jsii.data_type(
    jsii_type="cdk8s-grafana.DataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "access": "access",
        "name": "name",
        "type": "type",
        "description": "description",
        "labels": "labels",
        "namespace": "namespace",
        "url": "url",
    },
)
class DataSourceProps:
    def __init__(
        self,
        *,
        access: AccessType,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access: Access type of the data source.
        :param name: Name of the data source.
        :param type: Type of the data source.
        :param description: Description of the data source. Default: - no description
        :param labels: Labels to apply to the kubernetes resource. When adding a data source to a Grafana instance using ``grafana.addDataSource``, labels provided to Grafana will be automatically applied. Otherwise, labels must be added manually. Default: - no labels
        :param namespace: Namespace to apply to the kubernetes resource. When adding a data source to a Grafana instance using ``grafana.addDataSource``, the namespace will be automatically inherited. Default: - undefined (will be assigned to the 'default' namespace)
        :param url: URL of the data source. Most resources besides the 'testdata' data source type require this field in order to retrieve data. Default: - default url for data source type
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "access": access,
            "name": name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if labels is not None:
            self._values["labels"] = labels
        if namespace is not None:
            self._values["namespace"] = namespace
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def access(self) -> AccessType:
        '''Access type of the data source.'''
        result = self._values.get("access")
        assert result is not None, "Required property 'access' is missing"
        return typing.cast(AccessType, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the data source.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of the data source.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the data source.

        :default: - no description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels to apply to the kubernetes resource.

        When adding a data source to a Grafana instance using ``grafana.addDataSource``,
        labels provided to Grafana will be automatically applied. Otherwise,
        labels must be added manually.

        :default: - no labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace to apply to the kubernetes resource.

        When adding a data source to a Grafana instance using ``grafana.addDataSource``,
        the namespace will be automatically inherited.

        :default: - undefined (will be assigned to the 'default' namespace)
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''URL of the data source.

        Most resources besides the 'testdata' data source
        type require this field in order to retrieve data.

        :default: - default url for data source type
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Grafana(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk8s-grafana.Grafana",
):
    '''A Grafana instance.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        admin_password: typing.Optional[builtins.str] = None,
        admin_user: typing.Optional[builtins.str] = None,
        default_data_source: typing.Optional[DataSourceProps] = None,
        image: typing.Optional[builtins.str] = None,
        ingress: typing.Optional[builtins.bool] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        require_login: typing.Optional[builtins.bool] = None,
        service_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param admin_password: Default admin password. Default: "secret"
        :param admin_user: Default admin username. Default: "root"
        :param default_data_source: Default data source - equivalent to calling ``grafana.addDataSource``. Default: - no data source added
        :param image: Specify a custom image for Grafana. Default: "public.ecr.aws/ubuntu/grafana:latest"
        :param ingress: Create an ingress to provide external access to the Grafana cluster. Default: true
        :param labels: Labels to apply to all Grafana resources. Default: - { app: "grafana" }
        :param namespace: Namespace to apply to all Grafana resources. The Grafana Operator must be installed in this namespace for resources to be recognized. Default: - undefined (will be assigned to the 'default' namespace)
        :param require_login: Require login in order to view or manage dashboards. Default: false
        :param service_type: Type of service to be created (NodePort, ClusterIP or LoadBalancer). Default: ClusterIP
        '''
        props = GrafanaProps(
            admin_password=admin_password,
            admin_user=admin_user,
            default_data_source=default_data_source,
            image=image,
            ingress=ingress,
            labels=labels,
            namespace=namespace,
            require_login=require_login,
            service_type=service_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addDashboard")
    def add_dashboard(
        self,
        id: builtins.str,
        *,
        title: builtins.str,
        data_source_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        folder: typing.Optional[builtins.str] = None,
        json_model: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        plugins: typing.Optional[typing.Sequence["GrafanaPlugin"]] = None,
        refresh_rate: typing.Optional[cdk8s.Duration] = None,
        time_range: typing.Optional[cdk8s.Duration] = None,
    ) -> Dashboard:
        '''Creates a dashboard associated with a particular data source.

        By default,
        labels are automatically added so that the data source is detected by
        Grafana.

        :param id: -
        :param title: Title of the dashboard.
        :param data_source_variables: Specify a mapping from data source variables to data source names. This is only needed if you are importing an existing dashboard's JSON and it specifies variables within an "__inputs" field. Default: - no data source variables
        :param folder: Group dashboards into folders. Default: - default folder
        :param json_model: All other dashboard customizations.
        :param labels: Labels to apply to the kubernetes resource. When adding a dashboard to a Grafana instance using ``grafana.addDashboard``, labels provided to Grafana will be automatically applied. Otherwise, labels must be added manually. Default: - no labels
        :param namespace: Namespace to apply to the kubernetes resource. When adding a dashboard to a Grafana instance using ``grafana.addDashboard``, the namespace will be automatically inherited. Default: - undefined (will be assigned to the 'default' namespace)
        :param plugins: Specify plugins required by the dashboard.
        :param refresh_rate: Auto-refresh interval. Default: - 5 seconds
        :param time_range: Time range for the dashboard, e.g. last 6 hours, last 7 days, etc. Default: - 6 hours
        '''
        props = DashboardProps(
            title=title,
            data_source_variables=data_source_variables,
            folder=folder,
            json_model=json_model,
            labels=labels,
            namespace=namespace,
            plugins=plugins,
            refresh_rate=refresh_rate,
            time_range=time_range,
        )

        return typing.cast(Dashboard, jsii.invoke(self, "addDashboard", [id, props]))

    @jsii.member(jsii_name="addDataSource")
    def add_data_source(
        self,
        id: builtins.str,
        *,
        access: AccessType,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> DataSource:
        '''Adds a data source.

        By default, labels are automatically added so that
        the data source is detected by Grafana.

        :param id: -
        :param access: Access type of the data source.
        :param name: Name of the data source.
        :param type: Type of the data source.
        :param description: Description of the data source. Default: - no description
        :param labels: Labels to apply to the kubernetes resource. When adding a data source to a Grafana instance using ``grafana.addDataSource``, labels provided to Grafana will be automatically applied. Otherwise, labels must be added manually. Default: - no labels
        :param namespace: Namespace to apply to the kubernetes resource. When adding a data source to a Grafana instance using ``grafana.addDataSource``, the namespace will be automatically inherited. Default: - undefined (will be assigned to the 'default' namespace)
        :param url: URL of the data source. Most resources besides the 'testdata' data source type require this field in order to retrieve data. Default: - default url for data source type
        '''
        props = DataSourceProps(
            access=access,
            name=name,
            type=type,
            description=description,
            labels=labels,
            namespace=namespace,
            url=url,
        )

        return typing.cast(DataSource, jsii.invoke(self, "addDataSource", [id, props]))


@jsii.data_type(
    jsii_type="cdk8s-grafana.GrafanaPlugin",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "version": "version"},
)
class GrafanaPlugin:
    def __init__(self, *, name: builtins.str, version: builtins.str) -> None:
        '''
        :param name: Name of the plugin, e.g. "grafana-piechart-panel".
        :param version: Version of the plugin, e.g. "1.3.6".
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "version": version,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the plugin, e.g. "grafana-piechart-panel".'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Version of the plugin, e.g. "1.3.6".'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrafanaPlugin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk8s-grafana.GrafanaProps",
    jsii_struct_bases=[],
    name_mapping={
        "admin_password": "adminPassword",
        "admin_user": "adminUser",
        "default_data_source": "defaultDataSource",
        "image": "image",
        "ingress": "ingress",
        "labels": "labels",
        "namespace": "namespace",
        "require_login": "requireLogin",
        "service_type": "serviceType",
    },
)
class GrafanaProps:
    def __init__(
        self,
        *,
        admin_password: typing.Optional[builtins.str] = None,
        admin_user: typing.Optional[builtins.str] = None,
        default_data_source: typing.Optional[DataSourceProps] = None,
        image: typing.Optional[builtins.str] = None,
        ingress: typing.Optional[builtins.bool] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        require_login: typing.Optional[builtins.bool] = None,
        service_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_password: Default admin password. Default: "secret"
        :param admin_user: Default admin username. Default: "root"
        :param default_data_source: Default data source - equivalent to calling ``grafana.addDataSource``. Default: - no data source added
        :param image: Specify a custom image for Grafana. Default: "public.ecr.aws/ubuntu/grafana:latest"
        :param ingress: Create an ingress to provide external access to the Grafana cluster. Default: true
        :param labels: Labels to apply to all Grafana resources. Default: - { app: "grafana" }
        :param namespace: Namespace to apply to all Grafana resources. The Grafana Operator must be installed in this namespace for resources to be recognized. Default: - undefined (will be assigned to the 'default' namespace)
        :param require_login: Require login in order to view or manage dashboards. Default: false
        :param service_type: Type of service to be created (NodePort, ClusterIP or LoadBalancer). Default: ClusterIP
        '''
        if isinstance(default_data_source, dict):
            default_data_source = DataSourceProps(**default_data_source)
        self._values: typing.Dict[str, typing.Any] = {}
        if admin_password is not None:
            self._values["admin_password"] = admin_password
        if admin_user is not None:
            self._values["admin_user"] = admin_user
        if default_data_source is not None:
            self._values["default_data_source"] = default_data_source
        if image is not None:
            self._values["image"] = image
        if ingress is not None:
            self._values["ingress"] = ingress
        if labels is not None:
            self._values["labels"] = labels
        if namespace is not None:
            self._values["namespace"] = namespace
        if require_login is not None:
            self._values["require_login"] = require_login
        if service_type is not None:
            self._values["service_type"] = service_type

    @builtins.property
    def admin_password(self) -> typing.Optional[builtins.str]:
        '''Default admin password.

        :default: "secret"
        '''
        result = self._values.get("admin_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def admin_user(self) -> typing.Optional[builtins.str]:
        '''Default admin username.

        :default: "root"
        '''
        result = self._values.get("admin_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_data_source(self) -> typing.Optional[DataSourceProps]:
        '''Default data source - equivalent to calling ``grafana.addDataSource``.

        :default: - no data source added
        '''
        result = self._values.get("default_data_source")
        return typing.cast(typing.Optional[DataSourceProps], result)

    @builtins.property
    def image(self) -> typing.Optional[builtins.str]:
        '''Specify a custom image for Grafana.

        :default: "public.ecr.aws/ubuntu/grafana:latest"
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingress(self) -> typing.Optional[builtins.bool]:
        '''Create an ingress to provide external access to the Grafana cluster.

        :default: true
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels to apply to all Grafana resources.

        :default: - { app: "grafana" }
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace to apply to all Grafana resources.

        The Grafana Operator must be
        installed in this namespace for resources to be recognized.

        :default: - undefined (will be assigned to the 'default' namespace)
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def require_login(self) -> typing.Optional[builtins.bool]:
        '''Require login in order to view or manage dashboards.

        :default: false
        '''
        result = self._values.get("require_login")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def service_type(self) -> typing.Optional[builtins.str]:
        '''Type of service to be created (NodePort, ClusterIP or LoadBalancer).

        :default: ClusterIP
        '''
        result = self._values.get("service_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrafanaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessType",
    "Dashboard",
    "DashboardProps",
    "DataSource",
    "DataSourceProps",
    "Grafana",
    "GrafanaPlugin",
    "GrafanaProps",
]

publication.publish()

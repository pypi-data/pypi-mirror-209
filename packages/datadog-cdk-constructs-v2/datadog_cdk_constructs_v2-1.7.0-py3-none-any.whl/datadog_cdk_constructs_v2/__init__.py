'''
# Datadog CDK Constructs

[![NPM](https://img.shields.io/npm/v/datadog-cdk-constructs?color=blue&label=npm+cdk+v1)](https://www.npmjs.com/package/datadog-cdk-constructs)
[![NPM](https://img.shields.io/npm/v/datadog-cdk-constructs-v2?color=39a356&label=npm+cdk+v2)](https://www.npmjs.com/package/datadog-cdk-constructs-v2)
[![PyPI](https://img.shields.io/pypi/v/datadog-cdk-constructs?color=blue&label=pypi+cdk+v1)](https://pypi.org/project/datadog-cdk-constructs/)
[![PyPI](https://img.shields.io/pypi/v/datadog-cdk-constructs-v2?color=39a356&label=pypi+cdk+v2)](https://pypi.org/project/datadog-cdk-constructs-v2/)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](https://github.com/DataDog/datadog-cdk-constructs/blob/main/LICENSE)

Use this Datadog CDK Construct Library to deploy serverless applications using AWS CDK .

This CDK library automatically configures ingestion of metrics, traces, and logs from your serverless applications by:

* Installing and configuring the Datadog Lambda layers for your [Python](https://github.com/DataDog/datadog-lambda-layer-python), [Node.js](https://github.com/DataDog/datadog-lambda-layer-js), and [Java](https://docs.datadoghq.com/serverless/installation/java/?tab=awscdk) Lambda functions.
* Enabling the collection of traces and custom metrics from your Lambda functions.
* Managing subscriptions from the Datadog Forwarder to your Lambda and non-Lambda log groups.

## AWS CDK v1 vs AWS CDK v2

Two separate versions of Datadog CDK Constructs exist; `datadog-cdk-constructs` and `datadog-cdk-constructs-v2`. These are designed to work with `AWS CDK v1` and `AWS CDK v2` respectively.

* `datadog-cdk-constructs-v2` requires Node 14+, while `datadog-cdk-constructs-v1` supports Node 12+.
* Otherwise, the use of the two packages is identical.

## npm Package Installation:

For use with AWS CDK v2:

```
yarn add --dev datadog-cdk-constructs-v2
# or
npm install datadog-cdk-constructs-v2 --save-dev
```

For use with AWS CDK v1:

```
yarn add --dev datadog-cdk-constructs
# or
npm install datadog-cdk-constructs --save-dev
```

## PyPI Package Installation:

For use with AWS CDK v2:

```
pip install datadog-cdk-constructs-v2
```

For use with AWS CDK v1:

```
pip install datadog-cdk-constructs
```

### Note:

Pay attention to the output from your package manager as the `Datadog CDK Construct Library` has peer dependencies.

## Usage

### AWS CDK

* *If you are new to AWS CDK then check out this [workshop](https://cdkworkshop.com/15-prerequisites.html).*
* *The following examples assume the use of AWS CDK v2. If you're using CDK v1, import `datadog-cdk-constructs` rather than `datadog-cdk-constructs-v2`.*

Add this to your CDK stack:

```python
import { Datadog } from "datadog-cdk-constructs-v2";

const datadog = new Datadog(this, "Datadog", {
  nodeLayerVersion: <LAYER_VERSION>,
  pythonLayerVersion: <LAYER_VERSION>,
  javaLayerVersion: <LAYER_VERSION>,
  addLayers: <BOOLEAN>,
  extensionLayerVersion: "<EXTENSION_VERSION>",
  forwarderArn: "<FORWARDER_ARN>",
  createForwarderPermissions: <BOOLEAN>,
  flushMetricsToLogs: <BOOLEAN>,
  site: "<SITE>",
  apiKey: "{Datadog_API_Key}",
  apiKeySecretArn: "{Secret_ARN_Datadog_API_Key}",
  apiKmsKey: "{Encrypted_Datadog_API_Key}",
  enableDatadogTracing: <BOOLEAN>,
  enableMergeXrayTraces: <BOOLEAN>,
  enableDatadogLogs: <BOOLEAN>,
  injectLogContext: <BOOLEAN>,
  logLevel: <STRING>,
  env: <STRING>, //Optional
  service: <STRING>, //Optional
  version: <STRING>, //Optional
  tags: <STRING>, //Optional
});
datadog.addLambdaFunctions([<LAMBDA_FUNCTIONS>])
datadog.addForwarderToNonLambdaLogGroups([<LOG_GROUPS>])
```

## Source Code Integration

[Source code integration](https://docs.datadoghq.com/integrations/guide/source-code-integration/) is enabled by default through automatic lambda tagging, and will work if:

* The Datadog Github Integration is installed.
* Your datadog-cdk dependency satisfies either of the below versions:

  * `datadog-cdk-constructs-v2` >= 1.4.0
  * `datadog-cdk-constructs` >= 0.8.5

### Alternative Methods to Enable Source Code Integration

If the automatic implementation doesn't work for your case, please follow one of the two guides below.

**Note: these alternate guides only work for Typescript.**

<details>
  <summary>datadog-cdk version satisfied, but Datadog Github Integration NOT installed</summary>

If the Datadog Github Integration is not installed, you need to import the `datadog-ci` package and manually upload your Git metadata to Datadog.
We recommend you do this where your CDK Stack is initialized.

```python
const app = new cdk.App();

// Make sure to add @datadog/datadog-ci via your package manager
const datadogCi = require("@datadog/datadog-ci");
// Manually uploading Git metadata to Datadog.
datadogCi.gitMetadata.uploadGitCommitHash('{Datadog_API_Key}', '<SITE>')

const app = new cdk.App();
new ExampleStack(app, "ExampleStack", {});

app.synth();
```

</details>
<details>
  <summary>datadog-cdk version NOT satisfied</summary>

Change your initialization function as follows (note: we're changing this to pass just the `gitHash` value to the CDK):

```python
async function main() {
  // Make sure to add @datadog/datadog-ci via your package manager
  const datadogCi = require("@datadog/datadog-ci");
  const [, gitHash] = await datadogCi.gitMetadata.uploadGitCommitHash('{Datadog_API_Key}', '<SITE>')

  const app = new cdk.App();
  // Pass in the hash to the ExampleStack constructor
  new ExampleStack(app, "ExampleStack", {}, gitHash);
}
```

Ensure you call this function to initialize your stack.

In your stack constructor, change to add an optional `gitHash` parameter, and call `addGitCommitMetadata()`:

```python
export class ExampleStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps, gitHash?: string) {
    ...
    ...
    datadog.addGitCommitMetadata([<YOUR_FUNCTIONS>], gitHash)
  }
}
```

</details>

## Configuration

To further configure your Datadog construct, use the following custom parameters:

*Note*: The descriptions use the npm package parameters, but they also apply to the PyPI package parameters.

| npm package parameter | PyPI package parameter | Description |
| --- | --- | --- |
| `addLayers` | `add_layers` | Whether to add the Lambda Layers or expect the user to bring their own. Defaults to true. When true, the Lambda Library version variables are also required. When false, you must include the Datadog Lambda library in your functions' deployment packages. |
| `pythonLayerVersion` | `python_layer_version` | Version of the Python Lambda layer to install, such as 21. Required if you are deploying at least one Lambda function written in Python and `addLayers` is true. Find the latest version number [here](https://github.com/DataDog/datadog-lambda-python/releases). |
| `nodeLayerVersion` | `node_layer_version` | Version of the Node.js Lambda layer to install, such as 29. Required if you are deploying at least one Lambda function written in Node.js and `addLayers` is true. Find the latest version number from [here](https://github.com/DataDog/datadog-lambda-js/releases). |
| `javaLayerVersion` | `java_layer_version` | Version of the Java layer to install, such as 8. Required if you are deploying at least one Lambda function written in Java and `addLayers` is true. Find the latest version number in the [Serverless Java installation documentation](https://docs.datadoghq.com/serverless/installation/java/?tab=awscdk). **Note**: `extensionLayerVersion >= 25` and `javaLayerVersion >= 5` are required for the Datadog construct to instrument your Java functions properly. |
| `extensionLayerVersion` | `extension_layer_version` | Version of the Datadog Lambda Extension layer to install, such as 5. When `extensionLayerVersion` is set, `apiKey` (or if encrypted, `apiKMSKey` or `apiKeySecretArn`) needs to be set as well. When enabled, lambda function log groups will not be subscribed by the forwarder. Learn more about the Lambda extension [here](https://docs.datadoghq.com/serverless/datadog_lambda_library/extension/). |
| `forwarderArn` | `forwarder_arn` | When set, the plugin will automatically subscribe the Datadog Forwarder to the functions' log groups. Do not set `forwarderArn` when `extensionLayerVersion` is set. |
| `createForwarderPermissions` | `createForwarderPermissions` | When set to `true`, creates a Lambda permission on the the Datadog Forwarder per log group. Since the Datadog Forwarder has permissions configured by default, this is unnecessary in most use cases. |
| `flushMetricsToLogs` | `flush_metrics_to_logs` | Send custom metrics using CloudWatch logs with the Datadog Forwarder Lambda function (recommended). Defaults to `true` . If you disable this parameter, it's required to set `apiKey` (or if encrypted, `apiKMSKey` or `apiKeySecretArn`). |
| `site` | `site` | Set which Datadog site to send data. This is only used when `flushMetricsToLogs` is `false` or `extensionLayerVersion` is set. Possible values are `datadoghq.com`, `datadoghq.eu`, `us3.datadoghq.com`, `us5.datadoghq.com`, `ap1.datadoghq.com`, and `ddog-gov.com`. The default is `datadoghq.com`. |
| `apiKey` | `api_key` | Datadog API Key, only needed when `flushMetricsToLogs` is `false` or `extensionLayerVersion` is set. For more information about getting a Datadog API key, see the [API key documentation](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys). |
| `apiKeySecretArn` | `api_key_secret_arn` | The ARN of the secret storing the Datadog API key in AWS Secrets Manager. Use this parameter in place of `apiKey` when `flushMetricsToLogs` is `false` or `extensionLayer` is set. Remember to add the `secretsmanager:GetSecretValue` permission to the Lambda execution role. |
| `apiKmsKey` | `api_kms_key` | Datadog API Key encrypted using KMS. Use this parameter in place of `apiKey` when `flushMetricsToLogs` is `false` or `extensionLayerVersion` is set, and you are using KMS encryption. |
| `enableDatadogTracing` | `enable_datadog_tracing` | Enable Datadog tracing on your Lambda functions. Defaults to `true`. |
| `enableMergeXrayTraces` | `enable_merge_xray_traces` | Enable merging X-Ray traces on your Lambda functions. Defaults to `false`. |
| `enableDatadogLogs` | `enable_datadog_logs` | Send Lambda function logs to Datadog via the Datadog Lambda Extension.  Defaults to `true`. Note: This setting has no effect on logs sent via the Datadog Forwarder. |
| `enableSourceCodeIntegration` | `enable_source_code_integration` | Enable Datadog Source Code Integration, connecting your telemetry with application code in your Git repositories. This requires the Datadog Github Integration to work, otherwise please follow the [alternative method](#alternative-methods-to-enable-source-code-integration). Learn more [here](https://docs.datadoghq.com/integrations/guide/source-code-integration/). Defaults to `true`. |
| `injectLogContext` | `inject_log_context` | When set, the Lambda layer will automatically patch console.log with Datadog's tracing ids. Defaults to `true`. |
| `logLevel` | `log_level` | When set to `debug`, the Datadog Lambda Library and Extension will log additional information to help troubleshoot issues. |
| `env` | `env` | When set along with `extensionLayerVersion`, a `DD_ENV` environment variable is added to all Lambda functions with the provided value. When set along with `forwarderArn`, an `env` tag is added to all Lambda functions with the provided value. |
| `service` | `service` | When set along with `extensionLayerVersion`, a `DD_SERVICE` environment variable is added to all Lambda functions with the provided value. When set along with `forwarderArn`, a `service` tag is added to all Lambda functions with the provided value. |
| `version` | `version` | When set along with `extensionLayerVersion`, a `DD_VERSION` environment variable is added to all Lambda functions with the provided value. When set along with `forwarderArn`, a `version` tag is added to all Lambda functions with the provided value. |
| `tags` | `tags` | A comma separated list of key:value pairs as a single string. When set along with `extensionLayerVersion`, a `DD_TAGS` environment variable is added to all Lambda functions with the provided value. When set along with `forwarderArn`, the cdk parses the string and sets each key:value pair as a tag to all Lambda functions. |
| `enableColdStartTracing`      | `enable_cold_start_tracing` | Set to `false` to disable Cold Start Tracing. Used in NodeJS and Python. Defaults to `true`. |
| `coldStartTraceMinDuration`   | `min_cold_start_trace_duration` | Sets the minimum duration (in milliseconds) for a module load event to be traced via Cold Start Tracing. Number. Defaults to `3`. |
| `coldStartTraceSkipLibs`      | `cold_start_trace_skip_libs`| Optionally skip creating Cold Start Spans for a comma-separated list of libraries. Useful to limit depth or skip known libraries. Default depends on runtime. |
| `enableProfiling`             | `enable_profiling` | Enable the Datadog Continuous Profiler with `true`. Supported in Beta for NodeJS and Python. Defaults to `false`. |
| `encodeAuthorizerContext`     |`encode_authorizer_context` | When set to `true` for Lambda authorizers, the tracing context will be encoded into the response for propagation. Supported for NodeJS and Python. Defaults to `true`. |
| `decodeAuthorizerContext`     |`decode_authorizer_context` | When set to `true` for Lambdas that are authorized via Lambda authorizers, it will parse and use the encoded tracing context (if found). Supported for NodeJS and Python. Defaults to `true`.                         |
| `apmFlushDeadline` | Used to determine when to submit spans before a timeout occurs, in milliseconds. When the remaining time in an AWS Lambda invocation is less than the value set, the tracer attempts to submit the current active spans and all finished spans. Supported for NodeJS and Python. Defaults to `100` milliseconds. |
| `redirectHandler` | `redirect_handler` | When set to `false`, skip redirecting handler to the Datadog Lambda Library's handler. Useful when only instrumenting with Datadog Lambda Extension. Defaults to `true`. |

**Note**: Using the parameters above may override corresponding function level `DD_XXX` environment variables.

### Tracing

Enable X-Ray Tracing on your Lambda functions. For more information, see [CDK documentation](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-lambda.Tracing.html).

```python
import * as lambda from "aws-cdk-lib/aws-lambda";

const lambda_function = new lambda.Function(this, "HelloHandler", {
  runtime: lambda.Runtime.NODEJS_14_X,
  code: lambda.Code.fromAsset("lambda"),
  handler: "hello.handler",
  tracing: lambda.Tracing.ACTIVE,
});
```

### Nested Stacks

Add the Datadog CDK Construct to each stack you wish to instrument with Datadog. In the example below, we initialize the Datadog CDK Construct and call `addLambdaFunctions()` in both the `RootStack` and `NestedStack`.

```python
import { Datadog } from "datadog-cdk-constructs-v2";
import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";

class RootStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    new NestedStack(this, "NestedStack");

    const datadog = new Datadog(this, "Datadog", {
      nodeLayerVersion: <LAYER_VERSION>,
      pythonLayerVersion: <LAYER_VERSION>,
      javaLayerVersion: <LAYER_VERSION>,
      addLayers: <BOOLEAN>,
      forwarderArn: "<FORWARDER_ARN>",
      flushMetricsToLogs: <BOOLEAN>,
      site: "<SITE>",
      apiKey: "{Datadog_API_Key}",
      apiKeySecretArn: "{Secret_ARN_Datadog_API_Key}",
      apiKmsKey: "{Encrypted_Datadog_API_Key}",
      enableDatadogTracing: <BOOLEAN>,
      enableMergeXrayTraces: <BOOLEAN>,
      enableDatadogLogs: <BOOLEAN>,
      injectLogContext: <BOOLEAN>
    });
    datadog.addLambdaFunctions([<LAMBDA_FUNCTIONS>]);

  }
}

class NestedStack extends cdk.NestedStack {
  constructor(scope: Construct, id: string, props?: cdk.NestedStackProps) {
    super(scope, id, props);

    const datadog = new Datadog(this, "Datadog", {
      nodeLayerVersion: <LAYER_VERSION>,
      pythonLayerVersion: <LAYER_VERSION>,
      javaLayerVersion: <LAYER_VERSION>,
      addLayers: <BOOLEAN>,
      forwarderArn: "<FORWARDER_ARN>",
      flushMetricsToLogs: <BOOLEAN>,
      site: "<SITE>",
      apiKey: "{Datadog_API_Key}",
      apiKeySecretArn: "{Secret_ARN_Datadog_API_Key}",
      apiKmsKey: "{Encrypted_Datadog_API_Key}",
      enableDatadogTracing: <BOOLEAN>,
      enableMergeXrayTraces: <BOOLEAN>,
      enableDatadogLogs: <BOOLEAN>,
      injectLogContext: <BOOLEAN>
    });
    datadog.addLambdaFunctions([<LAMBDA_FUNCTIONS>]);

  }
}
```

### Tags

Add tags to your constructs. We recommend setting an `env` and `service` tag to tie Datadog telemetry together. For more information see [official AWS documentation](https://docs.aws.amazon.com/cdk/latest/guide/tagging.html) and [CDK documentation](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.Tags.html).

## How it works

The Datadog CDK construct takes in a list of lambda functions and installs the Datadog Lambda Library by attaching the Lambda Layers for [Java](https://docs.datadoghq.com/serverless/installation/java/?tab=awscdk), [Node.js](https://github.com/DataDog/datadog-lambda-layer-js), and [Python](https://github.com/DataDog/datadog-lambda-layer-python) to your functions. It redirects to a replacement handler that initializes the Lambda Library without any required code changes. Additional configurations added to the Datadog CDK construct will also translate into their respective environment variables under each lambda function (if applicable / required).

While Lambda function based log groups are handled by the `addLambdaFunctions` method automatically, the construct has an additional function `addForwarderToNonLambdaLogGroups` which subscribes the forwarder to any additional log groups of your choosing.

## Resources to learn about CDK

* [CDK TypeScript Workshop](https://cdkworkshop.com/20-typescript.html)
* [Video Introducing CDK by AWS with Demo](https://youtu.be/ZWCvNFUN-sU)
* [CDK Concepts](https://youtu.be/9As_ZIjUGmY)

## Repository Structure

In this repository, the folders `v1` and `v2` correspond to the packages `datadog-cdk-constructs` and `datadog-cdk-contructs-v2`. Each can be treated as a separate project (they are separate projen projects with separate dependencies, config files, tests, and scripts).

Additionally, there is a `common` folder that contains shared logic common to both `v1` and `v2` packages. This is done by soft-linking a `common` folder within `v1/src` and `v2/src` to the `common` folder in the root of the repository.

## Using Projen

The `v1` and `v2` Datadog CDK Construct Libraries both use Projen to maintain project configuration files such as the `package.json`, `.gitignore`, `.npmignore`, etc. Most of the configuration files will be protected by Projen via read-only permissions. In order to change these files, edit the `.projenrc.js` file within `v1` or `v2` folders, then run `npx projen` (while in `v1` or `v2`) to synthesize the new changes. Check out [Projen](https://github.com/projen/projen) for more details.

## Opening Issues

If you encounter a bug with this package, we want to hear about it. Before opening a new issue, search the existing issues to avoid duplicates.

When opening an issue, include the Datadog CDK Construct version, Node version, and stack trace if available. In addition, include the steps to reproduce when appropriate.

You can also open an issue for a feature request.

## Contributing

If you find an issue with this package and have a fix, please feel free to open a pull request following the [procedures](https://github.com/DataDog/datadog-cdk-constructs/blob/main/CONTRIBUTING.md).

## Testing

If you contribute to this package you can run the tests using `yarn test` within the `v1` or `v2` folders. This package also includes a sample application for manual testing:

1. Open a seperate terminal and `cd` into `v1` or `v2`.
2. Run `yarn watch`, this will ensure the Typescript files in the `src` directory are compiled to Javascript in the `lib` directory.
3. Navigate to `src/sample`, here you can edit `index.ts` to test your contributions manually.
4. At the root of the `v1` or `v2` directory (whichever you are working on), run `npx cdk --app lib/sample/index.js <CDK Command>`, replacing `<CDK Command>` with common CDK commands like `synth`, `diff`, or `deploy`.

* Note, if you receive "... is not authorized to perform: ..." you may also need to authorize the commands with your AWS credentials.

### Debug Logs

To display the debug logs for this library, set the `DD_CONSTRUCT_DEBUG_LOGS` env var to `true` when running `cdk synth` (use `--quiet` to suppress generated template output).

Example:
*Ensure you are at the root of the `v1` or `v2` directory*

```
DD_CONSTRUCT_DEBUG_LOGS=true npx cdk --app lib/sample/index.js synth --quiet
```

## Community

For product feedback and questions, join the `#serverless` channel in the [Datadog community on Slack](https://chat.datadoghq.com/).

## License

Unless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.

This product includes software developed at Datadog (https://www.datadoghq.com/). Copyright 2021 Datadog, Inc.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *


@jsii.data_type(
    jsii_type="datadog-cdk-constructs-v2.DatadogStrictProps",
    jsii_struct_bases=[],
    name_mapping={
        "add_layers": "addLayers",
        "capture_lambda_payload": "captureLambdaPayload",
        "enable_datadog_logs": "enableDatadogLogs",
        "enable_datadog_tracing": "enableDatadogTracing",
        "enable_merge_xray_traces": "enableMergeXrayTraces",
        "inject_log_context": "injectLogContext",
        "api_key": "apiKey",
        "api_key_secret_arn": "apiKeySecretArn",
        "api_kms_key": "apiKmsKey",
        "extension_layer_version": "extensionLayerVersion",
        "flush_metrics_to_logs": "flushMetricsToLogs",
        "forwarder_arn": "forwarderArn",
        "java_layer_version": "javaLayerVersion",
        "log_level": "logLevel",
        "node_layer_version": "nodeLayerVersion",
        "python_layer_version": "pythonLayerVersion",
        "redirect_handler": "redirectHandler",
        "site": "site",
        "source_code_integration": "sourceCodeIntegration",
    },
)
class DatadogStrictProps:
    def __init__(
        self,
        *,
        add_layers: builtins.bool,
        capture_lambda_payload: builtins.bool,
        enable_datadog_logs: builtins.bool,
        enable_datadog_tracing: builtins.bool,
        enable_merge_xray_traces: builtins.bool,
        inject_log_context: builtins.bool,
        api_key: typing.Optional[builtins.str] = None,
        api_key_secret_arn: typing.Optional[builtins.str] = None,
        api_kms_key: typing.Optional[builtins.str] = None,
        extension_layer_version: typing.Optional[jsii.Number] = None,
        flush_metrics_to_logs: typing.Optional[builtins.bool] = None,
        forwarder_arn: typing.Optional[builtins.str] = None,
        java_layer_version: typing.Optional[jsii.Number] = None,
        log_level: typing.Optional[builtins.str] = None,
        node_layer_version: typing.Optional[jsii.Number] = None,
        python_layer_version: typing.Optional[jsii.Number] = None,
        redirect_handler: typing.Optional[builtins.bool] = None,
        site: typing.Optional[builtins.str] = None,
        source_code_integration: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param add_layers: 
        :param capture_lambda_payload: 
        :param enable_datadog_logs: 
        :param enable_datadog_tracing: 
        :param enable_merge_xray_traces: 
        :param inject_log_context: 
        :param api_key: 
        :param api_key_secret_arn: 
        :param api_kms_key: 
        :param extension_layer_version: 
        :param flush_metrics_to_logs: 
        :param forwarder_arn: 
        :param java_layer_version: 
        :param log_level: 
        :param node_layer_version: 
        :param python_layer_version: 
        :param redirect_handler: 
        :param site: 
        :param source_code_integration: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0d4909ff321b27042bd7da99817517e719945ec07952fd9fd3a213ccaf8b9d4)
            check_type(argname="argument add_layers", value=add_layers, expected_type=type_hints["add_layers"])
            check_type(argname="argument capture_lambda_payload", value=capture_lambda_payload, expected_type=type_hints["capture_lambda_payload"])
            check_type(argname="argument enable_datadog_logs", value=enable_datadog_logs, expected_type=type_hints["enable_datadog_logs"])
            check_type(argname="argument enable_datadog_tracing", value=enable_datadog_tracing, expected_type=type_hints["enable_datadog_tracing"])
            check_type(argname="argument enable_merge_xray_traces", value=enable_merge_xray_traces, expected_type=type_hints["enable_merge_xray_traces"])
            check_type(argname="argument inject_log_context", value=inject_log_context, expected_type=type_hints["inject_log_context"])
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument api_key_secret_arn", value=api_key_secret_arn, expected_type=type_hints["api_key_secret_arn"])
            check_type(argname="argument api_kms_key", value=api_kms_key, expected_type=type_hints["api_kms_key"])
            check_type(argname="argument extension_layer_version", value=extension_layer_version, expected_type=type_hints["extension_layer_version"])
            check_type(argname="argument flush_metrics_to_logs", value=flush_metrics_to_logs, expected_type=type_hints["flush_metrics_to_logs"])
            check_type(argname="argument forwarder_arn", value=forwarder_arn, expected_type=type_hints["forwarder_arn"])
            check_type(argname="argument java_layer_version", value=java_layer_version, expected_type=type_hints["java_layer_version"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            check_type(argname="argument node_layer_version", value=node_layer_version, expected_type=type_hints["node_layer_version"])
            check_type(argname="argument python_layer_version", value=python_layer_version, expected_type=type_hints["python_layer_version"])
            check_type(argname="argument redirect_handler", value=redirect_handler, expected_type=type_hints["redirect_handler"])
            check_type(argname="argument site", value=site, expected_type=type_hints["site"])
            check_type(argname="argument source_code_integration", value=source_code_integration, expected_type=type_hints["source_code_integration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "add_layers": add_layers,
            "capture_lambda_payload": capture_lambda_payload,
            "enable_datadog_logs": enable_datadog_logs,
            "enable_datadog_tracing": enable_datadog_tracing,
            "enable_merge_xray_traces": enable_merge_xray_traces,
            "inject_log_context": inject_log_context,
        }
        if api_key is not None:
            self._values["api_key"] = api_key
        if api_key_secret_arn is not None:
            self._values["api_key_secret_arn"] = api_key_secret_arn
        if api_kms_key is not None:
            self._values["api_kms_key"] = api_kms_key
        if extension_layer_version is not None:
            self._values["extension_layer_version"] = extension_layer_version
        if flush_metrics_to_logs is not None:
            self._values["flush_metrics_to_logs"] = flush_metrics_to_logs
        if forwarder_arn is not None:
            self._values["forwarder_arn"] = forwarder_arn
        if java_layer_version is not None:
            self._values["java_layer_version"] = java_layer_version
        if log_level is not None:
            self._values["log_level"] = log_level
        if node_layer_version is not None:
            self._values["node_layer_version"] = node_layer_version
        if python_layer_version is not None:
            self._values["python_layer_version"] = python_layer_version
        if redirect_handler is not None:
            self._values["redirect_handler"] = redirect_handler
        if site is not None:
            self._values["site"] = site
        if source_code_integration is not None:
            self._values["source_code_integration"] = source_code_integration

    @builtins.property
    def add_layers(self) -> builtins.bool:
        result = self._values.get("add_layers")
        assert result is not None, "Required property 'add_layers' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def capture_lambda_payload(self) -> builtins.bool:
        result = self._values.get("capture_lambda_payload")
        assert result is not None, "Required property 'capture_lambda_payload' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def enable_datadog_logs(self) -> builtins.bool:
        result = self._values.get("enable_datadog_logs")
        assert result is not None, "Required property 'enable_datadog_logs' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def enable_datadog_tracing(self) -> builtins.bool:
        result = self._values.get("enable_datadog_tracing")
        assert result is not None, "Required property 'enable_datadog_tracing' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def enable_merge_xray_traces(self) -> builtins.bool:
        result = self._values.get("enable_merge_xray_traces")
        assert result is not None, "Required property 'enable_merge_xray_traces' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def inject_log_context(self) -> builtins.bool:
        result = self._values.get("inject_log_context")
        assert result is not None, "Required property 'inject_log_context' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def api_key(self) -> typing.Optional[builtins.str]:
        result = self._values.get("api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_key_secret_arn(self) -> typing.Optional[builtins.str]:
        result = self._values.get("api_key_secret_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_kms_key(self) -> typing.Optional[builtins.str]:
        result = self._values.get("api_kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extension_layer_version(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("extension_layer_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def flush_metrics_to_logs(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("flush_metrics_to_logs")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def forwarder_arn(self) -> typing.Optional[builtins.str]:
        result = self._values.get("forwarder_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def java_layer_version(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("java_layer_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_layer_version(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("node_layer_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def python_layer_version(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("python_layer_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def redirect_handler(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("redirect_handler")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def site(self) -> typing.Optional[builtins.str]:
        result = self._values.get("site")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_code_integration(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("source_code_integration")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatadogStrictProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="datadog-cdk-constructs-v2.IDatadogProps")
class IDatadogProps(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="addLayers")
    def add_layers(self) -> typing.Optional[builtins.bool]:
        ...

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> typing.Optional[builtins.str]:
        ...

    @builtins.property
    @jsii.member(jsii_name="apiKmsKey")
    def api_kms_key(self) -> typing.Optional[builtins.str]:
        ...

    @builtins.property
    @jsii.member(jsii_name="apmFlushDeadline")
    def apm_flush_deadline(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, jsii.Number]]:
        ...

    @builtins.property
    @jsii.member(jsii_name="captureLambdaPayload")
    def capture_lambda_payload(self) -> typing.Optional[builtins.bool]:
        ...

    @builtins.property
    @jsii.member(jsii_name="coldStartTraceSkipLibs")
    def cold_start_trace_skip_libs(self) -> typing.Optional[builtins.str]:
        ...

    @builtins.property
    @jsii.member(jsii_name="createForwarderPermissions")
    def create_forwarder_permissions(self) -> typing.Optional[builtins.bool]:
        ...

    @builtins.property
    @jsii.member(jsii_name="decodeAuthorizerContext")
    def decode_authorizer_context(self) -> typing.Optional[builtins.bool]:
        ...

    @builtins.property
    @jsii.member(jsii_name="enableColdStartTracing")
    def enable_cold_start_tracing(self) -> typing.Optional[builtins.bool]:
        ...

    @builtins.property
    @jsii.member(jsii_name="enableDatadogLogs")
    def enable_datadog_logs(self) -> typing.Optional[builtins.bool]:
        ...

    @builtins.property
    @jsii.member(jsii_name="enableDatadogTracing")
    def enable_datadog_tracing(self) -> typing.Optional[builtins.bool]:
        ...

    @builtins.property
    @jsii.member(jsii_name="enableMergeXrayTraces")
    def enable_merge_xray_traces(self) -> typing.Optional[builtins.bool]:
        ...

    @builtins.property
    @jsii.member(jsii_name="enableProfiling")
    def enable_profiling(self) -> typing.Optional[builtins.bool]:
        ...

    @builtins.property
    @jsii.member(jsii_name="encodeAuthorizerContext")
    def encode_authorizer_context(self) -> typing.Optional[builtins.bool]:
        ...

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> typing.Optional[builtins.str]:
        ...

    @builtins.property
    @jsii.member(jsii_name="extensionLayerVersion")
    def extension_layer_version(self) -> typing.Optional[jsii.Number]:
        ...

    @builtins.property
    @jsii.member(jsii_name="flushMetricsToLogs")
    def flush_metrics_to_logs(self) -> typing.Optional[builtins.bool]:
        ...

    @builtins.property
    @jsii.member(jsii_name="forwarderArn")
    def forwarder_arn(self) -> typing.Optional[builtins.str]:
        ...

    @builtins.property
    @jsii.member(jsii_name="injectLogContext")
    def inject_log_context(self) -> typing.Optional[builtins.bool]:
        ...

    @builtins.property
    @jsii.member(jsii_name="javaLayerVersion")
    def java_layer_version(self) -> typing.Optional[jsii.Number]:
        ...

    @builtins.property
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> typing.Optional[builtins.str]:
        ...

    @builtins.property
    @jsii.member(jsii_name="minColdStartTraceDuration")
    def min_cold_start_trace_duration(self) -> typing.Optional[jsii.Number]:
        ...

    @builtins.property
    @jsii.member(jsii_name="nodeLayerVersion")
    def node_layer_version(self) -> typing.Optional[jsii.Number]:
        ...

    @builtins.property
    @jsii.member(jsii_name="pythonLayerVersion")
    def python_layer_version(self) -> typing.Optional[jsii.Number]:
        ...

    @builtins.property
    @jsii.member(jsii_name="redirectHandler")
    def redirect_handler(self) -> typing.Optional[builtins.bool]:
        ...

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> typing.Optional[builtins.str]:
        ...

    @builtins.property
    @jsii.member(jsii_name="site")
    def site(self) -> typing.Optional[builtins.str]:
        ...

    @builtins.property
    @jsii.member(jsii_name="sourceCodeIntegration")
    def source_code_integration(self) -> typing.Optional[builtins.bool]:
        ...

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[builtins.str]:
        ...

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[builtins.str]:
        ...

    @builtins.property
    @jsii.member(jsii_name="apiKeySecretArn")
    def api_key_secret_arn(self) -> typing.Optional[builtins.str]:
        ...

    @api_key_secret_arn.setter
    def api_key_secret_arn(self, value: typing.Optional[builtins.str]) -> None:
        ...


class _IDatadogPropsProxy:
    __jsii_type__: typing.ClassVar[str] = "datadog-cdk-constructs-v2.IDatadogProps"

    @builtins.property
    @jsii.member(jsii_name="addLayers")
    def add_layers(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "addLayers"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKey"))

    @builtins.property
    @jsii.member(jsii_name="apiKmsKey")
    def api_kms_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKmsKey"))

    @builtins.property
    @jsii.member(jsii_name="apmFlushDeadline")
    def apm_flush_deadline(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, jsii.Number]]:
        return typing.cast(typing.Optional[typing.Union[builtins.str, jsii.Number]], jsii.get(self, "apmFlushDeadline"))

    @builtins.property
    @jsii.member(jsii_name="captureLambdaPayload")
    def capture_lambda_payload(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "captureLambdaPayload"))

    @builtins.property
    @jsii.member(jsii_name="coldStartTraceSkipLibs")
    def cold_start_trace_skip_libs(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "coldStartTraceSkipLibs"))

    @builtins.property
    @jsii.member(jsii_name="createForwarderPermissions")
    def create_forwarder_permissions(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createForwarderPermissions"))

    @builtins.property
    @jsii.member(jsii_name="decodeAuthorizerContext")
    def decode_authorizer_context(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "decodeAuthorizerContext"))

    @builtins.property
    @jsii.member(jsii_name="enableColdStartTracing")
    def enable_cold_start_tracing(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableColdStartTracing"))

    @builtins.property
    @jsii.member(jsii_name="enableDatadogLogs")
    def enable_datadog_logs(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableDatadogLogs"))

    @builtins.property
    @jsii.member(jsii_name="enableDatadogTracing")
    def enable_datadog_tracing(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableDatadogTracing"))

    @builtins.property
    @jsii.member(jsii_name="enableMergeXrayTraces")
    def enable_merge_xray_traces(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableMergeXrayTraces"))

    @builtins.property
    @jsii.member(jsii_name="enableProfiling")
    def enable_profiling(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableProfiling"))

    @builtins.property
    @jsii.member(jsii_name="encodeAuthorizerContext")
    def encode_authorizer_context(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "encodeAuthorizerContext"))

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "env"))

    @builtins.property
    @jsii.member(jsii_name="extensionLayerVersion")
    def extension_layer_version(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "extensionLayerVersion"))

    @builtins.property
    @jsii.member(jsii_name="flushMetricsToLogs")
    def flush_metrics_to_logs(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "flushMetricsToLogs"))

    @builtins.property
    @jsii.member(jsii_name="forwarderArn")
    def forwarder_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forwarderArn"))

    @builtins.property
    @jsii.member(jsii_name="injectLogContext")
    def inject_log_context(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "injectLogContext"))

    @builtins.property
    @jsii.member(jsii_name="javaLayerVersion")
    def java_layer_version(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "javaLayerVersion"))

    @builtins.property
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logLevel"))

    @builtins.property
    @jsii.member(jsii_name="minColdStartTraceDuration")
    def min_cold_start_trace_duration(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minColdStartTraceDuration"))

    @builtins.property
    @jsii.member(jsii_name="nodeLayerVersion")
    def node_layer_version(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nodeLayerVersion"))

    @builtins.property
    @jsii.member(jsii_name="pythonLayerVersion")
    def python_layer_version(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "pythonLayerVersion"))

    @builtins.property
    @jsii.member(jsii_name="redirectHandler")
    def redirect_handler(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "redirectHandler"))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "service"))

    @builtins.property
    @jsii.member(jsii_name="site")
    def site(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "site"))

    @builtins.property
    @jsii.member(jsii_name="sourceCodeIntegration")
    def source_code_integration(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "sourceCodeIntegration"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="apiKeySecretArn")
    def api_key_secret_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeySecretArn"))

    @api_key_secret_arn.setter
    def api_key_secret_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8575dd8c5598108689e31cffc5a95a627de8ad5238fb62faa9d01bb0af57870)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKeySecretArn", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatadogProps).__jsii_proxy_class__ = lambda : _IDatadogPropsProxy


@jsii.interface(jsii_type="datadog-cdk-constructs-v2.ILambdaFunction")
class ILambdaFunction(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="node")
    def node(self) -> "Node":
        ...

    @node.setter
    def node(self, value: "Node") -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> "Runtime":
        ...

    @runtime.setter
    def runtime(self, value: "Runtime") -> None:
        ...

    @jsii.member(jsii_name="addEnvironment")
    def add_environment(
        self,
        key: builtins.str,
        value: builtins.str,
        options: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param key: -
        :param value: -
        :param options: -
        '''
        ...


class _ILambdaFunctionProxy:
    __jsii_type__: typing.ClassVar[str] = "datadog-cdk-constructs-v2.ILambdaFunction"

    @builtins.property
    @jsii.member(jsii_name="node")
    def node(self) -> "Node":
        return typing.cast("Node", jsii.get(self, "node"))

    @node.setter
    def node(self, value: "Node") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fd9ea625d2ef267cd51675f7bc9ed93c806c411dc2ed28173160e9e99445ec2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "node", value)

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> "Runtime":
        return typing.cast("Runtime", jsii.get(self, "runtime"))

    @runtime.setter
    def runtime(self, value: "Runtime") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9982ab95a46df98104a3d1863d5bb0f9e9809ccc59137b73f0b2f7ff79e464a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtime", value)

    @jsii.member(jsii_name="addEnvironment")
    def add_environment(
        self,
        key: builtins.str,
        value: builtins.str,
        options: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param key: -
        :param value: -
        :param options: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c462515ef6fe1fe93f2a67a984d61b4df5cb4ecd80f6f33256b06e2ef756e774)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
        return typing.cast(None, jsii.invoke(self, "addEnvironment", [key, value, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILambdaFunction).__jsii_proxy_class__ = lambda : _ILambdaFunctionProxy


@jsii.data_type(
    jsii_type="datadog-cdk-constructs-v2.Node",
    jsii_struct_bases=[],
    name_mapping={"default_child": "defaultChild"},
)
class Node:
    def __init__(self, *, default_child: typing.Any) -> None:
        '''
        :param default_child: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b031a9a9356d281380eb23c847fc68b7a40ef4f9c9175b10723b3df950f40fd)
            check_type(argname="argument default_child", value=default_child, expected_type=type_hints["default_child"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_child": default_child,
        }

    @builtins.property
    def default_child(self) -> typing.Any:
        result = self._values.get("default_child")
        assert result is not None, "Required property 'default_child' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Node(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="datadog-cdk-constructs-v2.Runtime",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Runtime:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0639977270a81d2f0f42855c73d20a000172a5161638228ab6cd9a064a29942a)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Runtime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="datadog-cdk-constructs-v2.RuntimeType")
class RuntimeType(enum.Enum):
    NODE = "NODE"
    PYTHON = "PYTHON"
    JAVA = "JAVA"
    UNSUPPORTED = "UNSUPPORTED"


@jsii.enum(jsii_type="datadog-cdk-constructs-v2.TagKeys")
class TagKeys(enum.Enum):
    CDK = "CDK"
    ENV = "ENV"
    SERVICE = "SERVICE"
    VERSION = "VERSION"


class Transport(
    metaclass=jsii.JSIIMeta,
    jsii_type="datadog-cdk-constructs-v2.Transport",
):
    def __init__(
        self,
        flush_metrics_to_logs: typing.Optional[builtins.bool] = None,
        site: typing.Optional[builtins.str] = None,
        api_key: typing.Optional[builtins.str] = None,
        api_key_secret_arn: typing.Optional[builtins.str] = None,
        api_kms_key: typing.Optional[builtins.str] = None,
        extension_layer_version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param flush_metrics_to_logs: -
        :param site: -
        :param api_key: -
        :param api_key_secret_arn: -
        :param api_kms_key: -
        :param extension_layer_version: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0096d7b257dfe55c39e9a74f016968fe42afe4617f426d50fed2ef3441338d7)
            check_type(argname="argument flush_metrics_to_logs", value=flush_metrics_to_logs, expected_type=type_hints["flush_metrics_to_logs"])
            check_type(argname="argument site", value=site, expected_type=type_hints["site"])
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument api_key_secret_arn", value=api_key_secret_arn, expected_type=type_hints["api_key_secret_arn"])
            check_type(argname="argument api_kms_key", value=api_kms_key, expected_type=type_hints["api_kms_key"])
            check_type(argname="argument extension_layer_version", value=extension_layer_version, expected_type=type_hints["extension_layer_version"])
        jsii.create(self.__class__, self, [flush_metrics_to_logs, site, api_key, api_key_secret_arn, api_kms_key, extension_layer_version])

    @jsii.member(jsii_name="applyEnvVars")
    def apply_env_vars(self, lambdas: typing.Sequence[ILambdaFunction]) -> None:
        '''
        :param lambdas: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36b2b48b92acf28e2e8ffef9123831fc89362305a97cfed821d91c642a67dd86)
            check_type(argname="argument lambdas", value=lambdas, expected_type=type_hints["lambdas"])
        return typing.cast(None, jsii.invoke(self, "applyEnvVars", [lambdas]))

    @builtins.property
    @jsii.member(jsii_name="flushMetricsToLogs")
    def flush_metrics_to_logs(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "flushMetricsToLogs"))

    @flush_metrics_to_logs.setter
    def flush_metrics_to_logs(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87d37a95f6dd3d1a31b972e8a18e2e936cbf664a6115834cfcc7603f98c551a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flushMetricsToLogs", value)

    @builtins.property
    @jsii.member(jsii_name="site")
    def site(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "site"))

    @site.setter
    def site(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6f64e6254d5b2c7300d506cc6c873060cbbc2f69b870b7754d459d721bfc9fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "site", value)

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__972f96a848003a1b191a5a2b1b385eb8ae5537da456ee82835b121b2f7bee129)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="apiKeySecretArn")
    def api_key_secret_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeySecretArn"))

    @api_key_secret_arn.setter
    def api_key_secret_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a239562249ca542ce2cf0d1c83a0a743656792a47b3366d1ae3d031f42f5c3ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKeySecretArn", value)

    @builtins.property
    @jsii.member(jsii_name="apiKmsKey")
    def api_kms_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKmsKey"))

    @api_kms_key.setter
    def api_kms_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66a0c11321e5495d2118a192e3d4e7e1cc604ec8c806a36ab92a4dfc5dec7bfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="extensionLayerVersion")
    def extension_layer_version(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "extensionLayerVersion"))

    @extension_layer_version.setter
    def extension_layer_version(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5e4df65851315cbd779a7d51db28b4f9f2ff24e8d2030ab94830e4548e02f64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extensionLayerVersion", value)


__all__ = [
    "DatadogStrictProps",
    "IDatadogProps",
    "ILambdaFunction",
    "Node",
    "Runtime",
    "RuntimeType",
    "TagKeys",
    "Transport",
]

publication.publish()

def _typecheckingstub__c0d4909ff321b27042bd7da99817517e719945ec07952fd9fd3a213ccaf8b9d4(
    *,
    add_layers: builtins.bool,
    capture_lambda_payload: builtins.bool,
    enable_datadog_logs: builtins.bool,
    enable_datadog_tracing: builtins.bool,
    enable_merge_xray_traces: builtins.bool,
    inject_log_context: builtins.bool,
    api_key: typing.Optional[builtins.str] = None,
    api_key_secret_arn: typing.Optional[builtins.str] = None,
    api_kms_key: typing.Optional[builtins.str] = None,
    extension_layer_version: typing.Optional[jsii.Number] = None,
    flush_metrics_to_logs: typing.Optional[builtins.bool] = None,
    forwarder_arn: typing.Optional[builtins.str] = None,
    java_layer_version: typing.Optional[jsii.Number] = None,
    log_level: typing.Optional[builtins.str] = None,
    node_layer_version: typing.Optional[jsii.Number] = None,
    python_layer_version: typing.Optional[jsii.Number] = None,
    redirect_handler: typing.Optional[builtins.bool] = None,
    site: typing.Optional[builtins.str] = None,
    source_code_integration: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8575dd8c5598108689e31cffc5a95a627de8ad5238fb62faa9d01bb0af57870(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fd9ea625d2ef267cd51675f7bc9ed93c806c411dc2ed28173160e9e99445ec2(
    value: Node,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9982ab95a46df98104a3d1863d5bb0f9e9809ccc59137b73f0b2f7ff79e464a7(
    value: Runtime,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c462515ef6fe1fe93f2a67a984d61b4df5cb4ecd80f6f33256b06e2ef756e774(
    key: builtins.str,
    value: builtins.str,
    options: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b031a9a9356d281380eb23c847fc68b7a40ef4f9c9175b10723b3df950f40fd(
    *,
    default_child: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0639977270a81d2f0f42855c73d20a000172a5161638228ab6cd9a064a29942a(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0096d7b257dfe55c39e9a74f016968fe42afe4617f426d50fed2ef3441338d7(
    flush_metrics_to_logs: typing.Optional[builtins.bool] = None,
    site: typing.Optional[builtins.str] = None,
    api_key: typing.Optional[builtins.str] = None,
    api_key_secret_arn: typing.Optional[builtins.str] = None,
    api_kms_key: typing.Optional[builtins.str] = None,
    extension_layer_version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36b2b48b92acf28e2e8ffef9123831fc89362305a97cfed821d91c642a67dd86(
    lambdas: typing.Sequence[ILambdaFunction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87d37a95f6dd3d1a31b972e8a18e2e936cbf664a6115834cfcc7603f98c551a0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6f64e6254d5b2c7300d506cc6c873060cbbc2f69b870b7754d459d721bfc9fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__972f96a848003a1b191a5a2b1b385eb8ae5537da456ee82835b121b2f7bee129(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a239562249ca542ce2cf0d1c83a0a743656792a47b3366d1ae3d031f42f5c3ba(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66a0c11321e5495d2118a192e3d4e7e1cc604ec8c806a36ab92a4dfc5dec7bfa(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5e4df65851315cbd779a7d51db28b4f9f2ff24e8d2030ab94830e4548e02f64(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

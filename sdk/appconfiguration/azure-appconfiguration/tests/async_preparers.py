# coding: utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from preparers import AppConfigPreparer, trim_kwargs_from_test_function


def app_config_decorator_async(func, **kwargs):
    @AppConfigPreparer()
    async def wrapper(*args, **kwargs):
        appconfiguration_connection_string = kwargs.pop("appconfiguration_connection_string")
        kwargs['appconfiguration_connection_string'] = appconfiguration_connection_string
        
        trimmed_kwargs = {k:v for k, v in kwargs.items()}
        trim_kwargs_from_test_function(func, trimmed_kwargs)

        await func(*args, **trimmed_kwargs)

    return wrapper

def app_config_aad_decorator_async(func, **kwargs):
    @AppConfigPreparer()
    async def wrapper(*args, **kwargs):
        appconfiguration_endpoint_string = kwargs.pop("appconfiguration_endpoint_string")
        kwargs['appconfiguration_endpoint_string'] = appconfiguration_endpoint_string

        trimmed_kwargs = {k:v for k, v in kwargs.items()}
        trim_kwargs_from_test_function(func, trimmed_kwargs)

        await func(*args, **trimmed_kwargs)

    return wrapper

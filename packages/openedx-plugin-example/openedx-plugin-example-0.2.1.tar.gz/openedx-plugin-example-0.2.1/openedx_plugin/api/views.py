# coding=utf-8
"""
written by: Lawrence McDaniel
            https://lawrencemcdaniel.com

date:       jun-2019

usage:      implements a simple REST API using Django RestFramework
"""
from rest_framework import viewsets

# this repo
from openedx_plugin.models import Configuration

# this module
from .serializers import ConfigurationSerializer


class ConfigurationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer

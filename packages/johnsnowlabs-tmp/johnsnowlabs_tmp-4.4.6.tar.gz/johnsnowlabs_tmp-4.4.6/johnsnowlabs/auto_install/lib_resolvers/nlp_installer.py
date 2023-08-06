from abc import ABCMeta

from johnsnowlabs.abstract_base.lib_resolver import (
    Py4JJslLibDependencyResolverABC,
    PyInstallTypes,
)
from johnsnowlabs.py_models.url_dependency import UrlDependency
from johnsnowlabs.utils.enums import (
    LatestCompatibleProductVersion,
    ProductName,
    SparkVersion,
    JvmHardwareTarget,
)


class NlpLibResolver(Py4JJslLibDependencyResolverABC, metaclass=ABCMeta):
    has_m1_jar = True
    has_cpu_jars = True
    has_py_install = True
    has_gpu_jars = True
    product_name = ProductName.nlp
    lib_version = LatestCompatibleProductVersion.spark_nlp.value
    compatible_spark_versions = [SparkVersion.spark3xx.value]

    compatible_spark_to_jar_map = {
        SparkVersion.spark3xx: {
            JvmHardwareTarget.gpu: UrlDependency(
                url="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/spark-nlp-gpu-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.gpu,
                spark_version=SparkVersion.spark3xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            JvmHardwareTarget.m1: UrlDependency(
                url="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/spark-nlp-m1-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.m1,
                spark_version=SparkVersion.spark3xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            JvmHardwareTarget.cpu: UrlDependency(
                url="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/spark-nlp-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.cpu,
                spark_version=SparkVersion.spark3xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
        }
    }
    compatible_spark_to_py_map = {
        SparkVersion.spark3xx: {
            # TODO HARDCODE HASH!!! OR grap from enum or somwhere comfy. Maybe configs/settings file?
            PyInstallTypes.wheel: UrlDependency(
                url="https://files.pythonhosted.org/packages/ad/02/b86152a985aaa66d628b9d07263a5df640daaae32388cbbf38851677baf6/spark_nlp-{lib_version}-py2.py3-none-any.whl",
                dependency_type=PyInstallTypes.wheel,
                spark_version=SparkVersion.spark3xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            PyInstallTypes.tar: UrlDependency(
                url="https://files.pythonhosted.org/packages/35/89/87dc31013c9a4f1d0ce71b38e93172bad49652ec3f587a4d4e40c91b439e/spark-nlp-{lib_version}.tar.gz",
                dependency_type=PyInstallTypes.tar,
                spark_version=SparkVersion.spark3xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
        }
    }

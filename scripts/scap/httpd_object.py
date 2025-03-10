from dataclasses import dataclass

from scap.object_type_2 import ObjectType2

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#apache"


@dataclass
class HttpdObject(ObjectType2):
    """The httpd_object element is used by a httpd test to define the different
    httpd binary installed on a system.

    There is actually only one object relating to this and it is the
    collection of all httpd binaries. Therefore, there are no child
    entities defined. Any OVAL Test written to check version will
    reference the same httpd_object which is basically an empty object
    element. A tool that implements the httpd_test and collects the
    httpd_object must know how to find all the httpd binaries on the
    system and verify that they are in fact httpd binaries.
    """

    class Meta:
        name = "httpd_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#apache"

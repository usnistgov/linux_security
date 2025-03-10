from dataclasses import dataclass, field
from typing import Optional

from scap.artifacts_type import ArtifactsType
from scap.document_type import DocumentType
from scap.generator_type_3 import GeneratorType3
from scap.questionnaires_type import QuestionnairesType
from scap.questions_type import QuestionsType
from scap.results_type import ResultsType
from scap.test_actions_type import TestActionsType
from scap.variables_type_2 import VariablesType2

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class Ociltype:
    """
    The OCILType represents the primary content model for the OCIL.

    :ivar generator: The generator element contains information related
        to the generation of the file. Specifically, a generator
        contains information about the application used to create the
        file, when it was created, and the schema to use to validate it.
    :ivar document: This element contains document-level information,
        including title, descriptions, and notices.
    :ivar questionnaires: The questionnaires element contains all the
        questionnaire constructs defined within the document.
    :ivar test_actions: The test_actions element contains all the
        boolean, choice, string, and numeric test actions defined within
        the document.
    :ivar questions: The questions element contains all the boolean,
        choice, string, and numeric questions, and any other supporting
        elements (e.g. choice group) defined within the document.
    :ivar artifacts: The artifacts element contains all the artifact
        constructs to be retrieved (as necessary) during evaluation.
    :ivar variables: The variables element contains all the constant,
        local, and external variables available to be used within the
        document.
    :ivar results: The results element contains the results of an
        evaluation of the OCIL file. This includes records of all
        questionnaire results, question results, and test_action
        results.
    """

    class Meta:
        name = "OCILType"

    generator: Optional[GeneratorType3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
    document: Optional[DocumentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    questionnaires: Optional[QuestionnairesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
    test_actions: Optional[TestActionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
    questions: Optional[QuestionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
    artifacts: Optional[ArtifactsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    variables: Optional[VariablesType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    results: Optional[ResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )

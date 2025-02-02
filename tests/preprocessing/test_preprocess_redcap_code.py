import pytest
from rarelink.preprocessing import parse_redcap_code
from phenopacket_mapper.data_standards import CodeSystem, Coding

@pytest.fixture
def resources():
    return [
        CodeSystem(name='SNOMED CT', namespace_prefix='SNOMED', url='https://www.snomed.org/snomed-ct'),
        CodeSystem(name='Monarch Disease Ontology', namespace_prefix='MONDO', url='https://mondo.monarchinitiative.org/'),
        CodeSystem(name='Human Phenotype Ontology', namespace_prefix='HP', url='https://hpo.jax.org/'),
        CodeSystem(name='Online Mendelian Inheritance', namespace_prefix='OMIM', url='https://omim.org/'),
        CodeSystem(name='Orphanet', namespace_prefix='ORDO', url='https://www.orpha.net/consor/cgi-bin/index.php'),
        CodeSystem(name='NCBI organismal classification', namespace_prefix='NCBITAXON', url='https://www.ncbi.nlm.nih.gov/taxonomy'),
        CodeSystem(name='Logical Observation Identifiers Names and Codes', namespace_prefix='LOINC', url='https://loinc.org/'),
        CodeSystem(name='HUGO Gene Nomenclature Committee', namespace_prefix='HGNC', url='https://www.genenames.org/'),
        CodeSystem(name='GENO: The Genotype Ontology', namespace_prefix='GENO', url='http://www.genoontology.org/'),
        CodeSystem(name='National Cancer Institute Thesaurus (NCIT)', namespace_prefix='NCIT', url='https://ncithesaurus.org/'),
        CodeSystem(name='Sequence Ontology (SO)', namespace_prefix='SO', url='http://www.sequenceontology.org/'),
        CodeSystem(name='International Classification of Diseases', namespace_prefix='ICD10CM', url='https://www.cdc.gov/nchs/icd/icd10cm.htm'),
        CodeSystem(name='International Classification of Diseases', namespace_prefix='ICD10', url='https://www.cdc.gov/nchs/icd/icd10cm.htm'),
        CodeSystem(name='ICD-11', namespace_prefix='ICD11', url='https://icd.who.int/en'),
        CodeSystem(name='HL7 FHIR', namespace_prefix='HL7FHIR', url='https://www.hl7.org/fhir/'),
        CodeSystem(name='Global Alliance for Genomics and Health Phenopacket Schema', namespace_prefix='GA4GH', url='https://www.ga4gh.org/'),
    ]

@pytest.mark.parametrize("input, expected", [
    ("snomed_410605003", Coding(system=CodeSystem(name='SNOMED CT', namespace_prefix='SNOMED', url='https://www.snomed.org/snomed-ct'), code='410605003')),
    ("mondo_0968976", Coding(system=CodeSystem(name='Monarch Disease Ontology', namespace_prefix='MONDO', url='https://mondo.monarchinitiative.org/'), code='0968976')),
    ("hp_4000034", Coding(system=CodeSystem(name='Human Phenotype Ontology', namespace_prefix='HP', url='https://hpo.jax.org/'), code='4000034')),
    ("HP:4000034", Coding(system=CodeSystem(name='Human Phenotype Ontology', namespace_prefix='HP', url='https://hpo.jax.org/'), code='4000034')),
    ("omim_147920", Coding(system=CodeSystem(name='Online Mendelian Inheritance', namespace_prefix='OMIM', url='https://omim.org/'), code='147920')),
    ("ordo_2322", Coding(system=CodeSystem(name='Orphanet', namespace_prefix='ORDO', url='https://www.orpha.net/consor/cgi-bin/index.php'), code='2322')),
    ("ncbitaxon_399550", Coding(system=CodeSystem(name='NCBI organismal classification', namespace_prefix='NCBITAXON', url='https://www.ncbi.nlm.nih.gov/taxonomy'), code='399550')),
    ("loinc_81304_8", Coding(system=CodeSystem(name='Logical Observation Identifiers Names and Codes', namespace_prefix='LOINC', url='https://loinc.org/'), code='81304-8')),
    ("hgnc_6382", Coding(system=CodeSystem(name='HUGO Gene Nomenclature Committee', namespace_prefix='HGNC', url='https://www.genenames.org/'), code='6382')),
    ("geno_00000", Coding(system=CodeSystem(name='GENO: The Genotype Ontology', namespace_prefix='GENO', url='http://www.genoontology.org/'), code='00000')),
    ("ncit_00000", Coding(system=CodeSystem(name='National Cancer Institute Thesaurus (NCIT)', namespace_prefix='NCIT', url='https://ncithesaurus.org/'), code='00000')),
    ("so_00000", Coding(system=CodeSystem(name='Sequence Ontology (SO)', namespace_prefix='SO', url='http://www.sequenceontology.org/'), code='00000')),
    ("icd10cm_R51_1", Coding(system=CodeSystem(name='International Classification of Diseases', namespace_prefix='ICD10CM', url='https://www.cdc.gov/nchs/icd/icd10cm.htm'), code='R51.1')),
    ("icd10_r51_2", Coding(system=CodeSystem(name='International Classification of Diseases', namespace_prefix='ICD10', url='https://icd.who.int/en'), code='R51.2')),
    ("icd11_r51_2", Coding(system=CodeSystem(name='ICD-11', namespace_prefix='ICD11', url='https://icd.who.int/en'), code='R51.2')),
    ("hl7fhir_123", Coding(system=CodeSystem(name='HL7 FHIR', namespace_prefix='HL7FHIR', url='https://www.hl7.org/fhir/'), code='123')),
    ("ga4gh_456", Coding(system=CodeSystem(name='GA4GH', namespace_prefix='GA4GH', url='https://www.ga4gh.org/'), code='456')),

])
def test_preprocess_redcap_code(input, resources, expected):
    assert parse_redcap_code(input, resources) == expected
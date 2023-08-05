import json


class ClassDescriptionOntology:
    def __init__(self, ontology):
        if type(ontology) == str:
            if ontology.endswith(".json"):
                with open(ontology, "r") as f:
                    ontology = json.load(f)
        elif type(ontology) == dict:
            ontology = ontology

        if ontology is None:
            raise ValueError("ontology must be a dict or a path to a json file")

        supported_ontologies = ["class_descriptions"]

        if ontology["ontology_type"] not in ["class_descriptions"]:
            raise (
                ValueError("ontology must be one of " + ", ".join(supported_ontologies))
            )

        self.ontology = ontology

        has_non_text_prompt = False
        for prompt in ontology["prompts"]:
            if prompt["prompt_type"] != "text":
                has_non_text_prompt = True
                break
        if has_non_text_prompt:
            raise ("classDescriptionOntology only supports text prompts")

        self.class_names = [
            cls_def["class_name"] for cls_def in self.ontology["prompts"]
        ]
        self.descriptions = [
            cls_def["prompt_value"] for cls_def in self.ontology["prompts"]
        ]

        self.class_name_to_description = {
            cls_def["class_name"]: cls_def["prompt_value"]
            for cls_def in self.ontology["prompts"]
        }
        self.description_to_class_name = {
            cls_def["prompt_value"]: cls_def["class_name"]
            for cls_def in self.ontology["prompts"]
        }

        self.class_ids = list(range(len(self.class_names)))

        self.class_id_map = {
            class_id: class_name for class_id, class_name in enumerate(self.class_names)
        }

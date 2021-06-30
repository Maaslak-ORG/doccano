import json
import os

from rest_framework.renderers import JSONRenderer

from api.models import Project, DOCUMENT_CLASSIFICATION, SEQUENCE_LABELING
from api.serializers import LabelSerializer
from api.utils import JSONPainter


def extract_document_classification(label, labels):
    return labels.get(pk=label["label"]).text


def extract_label_seq_labeling(label, labels):
    return [
        label["start_offset"],
        label["end_offset"],
        labels.get(pk=label["label"]).text,
    ]


def get_extract_label(project):
    return {
        DOCUMENT_CLASSIFICATION: extract_document_classification,
        SEQUENCE_LABELING: extract_label_seq_labeling,
    }[project.project_type]


def get_all_projects_json():
    dump_dir = "projects_dump"
    if not os.path.exists(dump_dir):
        os.makedirs(dump_dir)
    for project in Project.objects.all():
        try:
            project_dir = f"{dump_dir}/dump_{project.name.replace('/', '_')}"
            if not os.path.exists(project_dir):
                os.makedirs(project_dir)
            print(f"Dumping {project.name}")
            labels = project.labels.all()
            label_serializer = LabelSerializer(labels, many=True)
            documents = project.documents.all()
            data = JSONPainter().paint(documents)
            data = map(
                lambda x: {
                    **x,
                    "labels": list(
                        map(
                            lambda y: get_extract_label(project)(y, labels),
                            x["annotations"],
                        )
                    ),
                },
                data,
            )
            data = map(json.dumps, data)
            data = map(lambda x: x + "\n", data)
            with open(f"{project_dir}/labels.json", "wb") as f:
                f.write(JSONRenderer().render(label_serializer.data))
            with open(f"{project_dir}/data.jsonl", "w") as f:
                f.writelines(data)
        except Exception as ex:
            print(f"Error {project.name} {ex}")

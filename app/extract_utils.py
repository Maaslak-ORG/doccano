import json
import os

from api.models import Project
from api.utils import JSONPainter


def get_all_projects_json():
    dump_dir = "projects_dump"
    if not os.path.exists(dump_dir):
        os.makedirs(dump_dir)

    for project in Project.objects.all():
        try:
            print(f"Dumping {project.name}")
            documents = project.documents.all()
            labels = project.labels.all()
            data = JSONPainter.paint_labels(documents, labels)
            data = map(json.dumps, data)
            # TODO translate project name slashes
            # with open(f"{dump_dir}/dump_{project.name.replace('/', '_')}", "w") as f:
            #     f.writelines(data)
        except Exception as ex:
            print(f"Error {project.name} {ex}")

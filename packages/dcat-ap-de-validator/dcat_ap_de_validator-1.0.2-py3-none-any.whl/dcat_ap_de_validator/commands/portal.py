import json
from dcat_ap_de_validator.portals import Portal, CKAN, DKAN
from dcat_ap_de_validator.metadata.validate import validate


def execute(args):
    portal_type = str(args.portal_type)
    portal = Portal(args.url)
    if portal_type.lower() == "dkan":
        portal = DKAN(args.url)
    else:
        portal = CKAN(args.url)
    package_list = portal.packages()
    portal_title = portal.get_title()
    validation_result = {"portal": portal_title, "warnings": 0, "errors": 0, "infos": 0, "valid_datasets": 0,"results": []}
    results = []

    for package_name in package_list:
        result = validate(portal.package_metadata_url(package_name))
        # count errors and warnings, successes
        validation_result["warnings"] += result["warning"]
        validation_result["errors"] += result["error"]
        validation_result["infos"] += result["info"]
        if result.get("valid", False):
            validation_result["valid_datasets"] += 1
        results.append({"package": package_name, "url": portal.package_url(package_name), "result": result})

    validation_result["results"] = results
    with open(f"{portal_title}.json", "w") as f:
        json.dump(validation_result, f)

    return validation_result

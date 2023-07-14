from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

projectLists = {"ProjectA": 100, "ProjectB": 130,
                "ProjectC": 160, "ProjectD": 190, "ProjectE": 220}

projectServiceList = {
    "ProjectA": {"Services": {"Ec2": 10, "Ec2 Other": 20, "Amazon Simple Storage Service": 30, "Aws Key management service": 40}},
    "ProjectB": {"Services": {"Ec2": 15, "Ec2 Other": 30, "Amazon Simple Storage Service": 35, "Aws Key management service": 50}},
    "ProjectC": {"Services": {"Ec2": 20, "Ec2 Other": 40, "Amazon Simple Storage Service": 40, "Aws Key management service": 60}},
    "ProjectD": {"Services": {"Ec2": 25, "Ec2 Other": 50, "Amazon Simple Storage Service": 45, "Aws Key management service": 70}},
    "ProjectE": {"Services": {"Ec2": 30, "Ec2 Other": 60, "Amazon Simple Storage Service": 50, "Aws Key management service": 80}}
}

def getProjectServices(projectName):
    projectRegistry = CollectorRegistry()
    projectGauge = Gauge(f"{projectName}_Services_Cost", "XC3 Project Breakdown Spend Cost",
                         labelnames=["project_spend_services",
                                     "project_spend_cost"],
                         registry=projectRegistry)
    
    if projectName in projectServiceList.keys():
        services = projectServiceList[projectName]["Services"]
        if services:
            for service, cost in services.items():
                projectGauge.labels(service, cost).set(cost)
                push_to_gateway("pushgateway:9091", job=f"{projectName}_service", registry=projectRegistry)
    print(projectGauge)

def getProjects():
    registry = CollectorRegistry()

    gauge = Gauge("Project_Spend_Cost", "XC3 Project Spend Cost",
                labelnames=["project_spend_project", "project_spend_cost"],
                registry=registry)

    projectNameList = list(projectLists.keys())
    for project in projectLists.items():
        projectName = project[0]
        projectCost = project[1]
        gauge.labels(projectName, projectCost).set(projectCost)

    print(gauge)

    push_to_gateway("pushgateway:9091", job="project_cost", registry=registry)

    for projectName in projectNameList:
        getProjectServices(projectName)

getProjects()
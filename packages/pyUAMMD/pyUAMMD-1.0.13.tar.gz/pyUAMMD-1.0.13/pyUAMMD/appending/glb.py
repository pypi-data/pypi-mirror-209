import copy
import logging

from ..utils.common import getDataEntryLabelIndex

def appendGlobal(globalKey,sim,sim2app,mode):

    logger = logging.getLogger("pyUAMMD")

    #########################
    #Appending global data
    #Global data structure:
    #   globalKey: {
    #       "parameters": {"temperature": ..., "box": [...,...,...], ...},
    #       "labels": ["name", "mass", "radius", "charge", ...],
    #       "data": [[...],
    #                [...],
    #                ...]

    # Four cases:
    # 1) global NOT in sim and global NOT in sim2app
    # 2) global NOT in sim and global in sim2app
    # 3) global in sim and global NOT in sim2app
    # 4) global in sim and global in sim2app

    globalInSim     = (globalKey in sim)
    globalInSim2app = (globalKey in sim2app)

    # 1) global NOT in sim and global NOT in sim2app
    if not globalInSim and not globalInSim2app:
        #Do nothing
        pass
    # 2) global NOT in sim and global in sim2app
    elif not globalInSim and globalInSim2app:
        sim[globalKey] = copy.deepcopy(sim2app[globalKey])
    # 3) global in sim and global NOT in sim2app
    elif globalInSim and not globalInSim2app:
        #Do nothing
        pass
    # 4) global in sim and global in sim2app
    elif globalInSim and globalInSim2app:

        #Process parameters

        parametersInSim     = ("parameters" in sim[globalKey])
        parametersInSim2app = ("parameters" in sim2app[globalKey])

        if not parametersInSim and not parametersInSim2app:
            #Do nothing
            pass
        elif not parametersInSim and parametersInSim2app:
            sim[globalKey]["parameters"] = copy.deepcopy(sim2app[globalKey]["parameters"])
        elif parametersInSim and not parametersInSim2app:
            #Do nothing
            pass
        elif parametersInSim and parametersInSim2app:

            #Check if parameters share some keys. If yes, check if they are the same.
            #If parameters do not share some keys or the shared keys are the same, append them.
            for key in sim[globalKey]["parameters"]:
                if key in sim2app[globalKey]["parameters"]:
                    if sim[globalKey]["parameters"][key] != sim2app[globalKey]["parameters"][key]:
                        logger.error("Shared global parameters are not the same")
                        raise Exception("Shared global parameters are not the same")
            sim[globalKey]["parameters"].update(sim2app[globalKey]["parameters"])

        #Process types
        typesInSim     = ("labels" in sim[globalKey])
        typesInSim2app = ("labels" in sim2app[globalKey])

        if not typesInSim and not typesInSim2app:
            #Do nothing
            pass
        elif not typesInSim and typesInSim2app:
            sim[globalKey]["labels"] = copy.deepcopy(sim2app[globalKey]["labels"])

            if "data" not in sim[globalKey]:
                sim[globalKey]["data"] = []

            sim[globalKey]["data"].extend(copy.deepcopy(sim2app[globalKey]["data"]))
        elif typesInSim and not typesInSim2app:
            #Do nothing
            pass
        elif typesInSim and typesInSim2app:

            #Check if global data are the same
            if sim[globalKey]["labels"] != sim2app[globalKey]["labels"]:
                logger.error("Global data labels are not the same")
                raise Exception("Global data labels are not the same")

            #At this point labels and parameters are the same, so we can append data.
            nameIndex     = getDataEntryLabelIndex(sim[globalKey],"name")
            nameIndex2app = getDataEntryLabelIndex(sim2app[globalKey],"name")

            #Iterate over data in sim2app
            for d in sim2app[globalKey]["data"]:
                #Check if name is already in sim. If not, append data.
                #If name is already in sim, check if data are the same. If not, raise error.
                if d[nameIndex2app] not in [x[nameIndex] for x in sim[globalKey]["data"]]:
                    sim[globalKey]["data"].append(d)
                else:
                    for x in sim[globalKey]["data"]:
                        if x[nameIndex] == d[nameIndex2app]:
                            if x != d:
                                logger.error("Shared type name. But type data are not the same")
                                raise Exception("Shared type name. But type data are not the same")

    #Global data appended
    #########################

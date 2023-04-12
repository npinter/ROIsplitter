// ExAnno v1.0
// Niko Pinter
// Extract cell detection based annotations (classifications) from QuPath TMA projects

import com.fasterxml.jackson.databind.JsonSerializer
import qupath.lib.scripting.QP

boolean prettyPrint = true

def gson = GsonTools.getInstance(prettyPrint)
def imageData = getCurrentImageData()

def TMAGrid = QP.getCurrentImageData().getHierarchy().TMAGrid

// Define output path (relative to project)
def tma_name = GeneralTools.getNameWithoutExtension(imageData.getServer().getMetadata().getName())
def outputDir = buildFilePath(PROJECT_BASE_DIR, "annotations_export_" + tma_name)
mkdirs(outputDir)

// Get image dimensions
def dim_w = getCurrentImageData().getServer().getWidth()
def dim_h = getCurrentImageData().getServer().getHeight()

// iterate over TMAGrid
def TMAGridList = TMAGrid.getTMACoreList()

for(core in TMAGridList) {
    def TMAjson = gson.toJson(TMAGrid.getTMACore(core.name).childObjects)
    def path = buildFilePath(outputDir, "annotations_TMA_"+core.name+".geojson")
    def featureNames = TMAGrid.getTMACore(core.name).childObjects.displayedName.unique()

    new File(path).write(
            '{ ' +
                    '"name": "' + core.name + '",' +
                    '"featureNames":' + gson.toJson(featureNames) + ',' +
                    '"dim": {' +
                    '"width": '+ dim_w +', "height": '+dim_h+'},' +
                    '"type": "FeatureCollection",' +
                    '"features":'+TMAjson+
            '}')
}

println "Done"
import {
  AbsoluteFill,
  CanvasImage,
  Composition,
  Folder,
  Still,
  staticFile,
  useCurrentFrame,
} from "remotion";
import {featherRectMask, type Rect} from "../ql01-pilot/feather-mask";
import {pageConfigs, type LayerConfig, type PageConfig} from "./page-config";

const WIDTH = 1920;
const HEIGHT = 1080;

type RenderEntry = {
  readonly page: PageConfig;
  readonly rects: readonly Rect[];
  readonly feathers: readonly number[];
};

const flattenRects = (rects: readonly Rect[]) => {
  const values: number[] = [];
  for (const rect of rects) {
    values.push(rect.x, rect.y, rect.width, rect.height);
  }
  return values;
};

const cropProps = (rect: Rect) => ({
  cropLeft: rect.x / WIDTH,
  cropRight: (WIDTH - rect.x - rect.width) / WIDTH,
  cropTop: rect.y / HEIGHT,
  cropBottom: (HEIGHT - rect.y - rect.height) / HEIGHT,
});

const getLayerFeather = (page: PageConfig, layer: LayerConfig) => {
  if (page.page === "QL-04") {
    return 10;
  }
  if (page.page === "QL-03" && layer.name === "结果") {
    return 2;
  }
  if (layer.name.includes("场景")) {
    return 28;
  }
  if (layer.rects.every((rect) => rect.height <= 130)) {
    return 10;
  }
  return 18;
};

const toLayerEntry = (page: PageConfig, layer: LayerConfig): RenderEntry => ({
  page,
  rects: layer.rects,
  feathers: layer.rects.map(() => getLayerFeather(page, layer)),
});

const toCombinedEntry = (page: PageConfig): RenderEntry => {
  if (page.combinedRects && page.combinedFeathers) {
    return {
      page,
      rects: page.combinedRects,
      feathers: page.combinedFeathers,
    };
  }
  const rects: Rect[] = [];
  const feathers: number[] = [];
  for (const layer of page.layers) {
    const feather = getLayerFeather(page, layer);
    for (const rect of layer.rects) {
      rects.push(rect);
      feathers.push(feather);
    }
  }
  return {page, rects, feathers};
};

const transparentEntries: RenderEntry[] = [];
for (const page of pageConfigs) {
  for (const layer of page.layers) {
    transparentEntries.push(toLayerEntry(page, layer));
  }
  transparentEntries.push(toCombinedEntry(page));
}

const SourceWithMask: React.FC<RenderEntry> = ({page, rects, feathers}) => {
  const nativeCrop = rects.length === 1 ? cropProps(rects[0]) : {};
  return (
    <CanvasImage
      src={staticFile(page.source)}
      style={{position: "absolute", left: 0, top: 0, width: WIDTH, height: HEIGHT}}
      effects={[
        featherRectMask({
          rects: flattenRects(rects),
          feather: 18,
          feathers,
        }),
      ]}
      {...nativeCrop}
    />
  );
};

const TransparentEntry: React.FC<RenderEntry> = (entry) => (
  <AbsoluteFill style={{backgroundColor: "transparent"}}>
    <SourceWithMask {...entry} />
  </AbsoluteFill>
);

const CheckerboardEntry: React.FC<RenderEntry> = (entry) => (
  <AbsoluteFill
    style={{
      backgroundColor: "#d9dee7",
      backgroundImage:
        "linear-gradient(45deg, #f6f7f9 25%, transparent 25%), linear-gradient(-45deg, #f6f7f9 25%, transparent 25%), linear-gradient(45deg, transparent 75%, #f6f7f9 75%), linear-gradient(-45deg, transparent 75%, #f6f7f9 75%)",
      backgroundPosition: "0 0, 0 24px, 24px -24px, -24px 0px",
      backgroundSize: "48px 48px",
    }}
  >
    <SourceWithMask {...entry} />
  </AbsoluteFill>
);

const BatchTransparent: React.FC = () => {
  const frame = useCurrentFrame();
  return <TransparentEntry {...transparentEntries[frame]} />;
};

const BatchCheckerboards: React.FC = () => {
  const frame = useCurrentFrame();
  return <CheckerboardEntry {...toCombinedEntry(pageConfigs[frame])} />;
};

export const QLBatchCompositions: React.FC = () => (
  <>
    <Composition
      id="QL-Batch-Transparent"
      component={BatchTransparent}
      durationInFrames={transparentEntries.length}
      fps={1}
      width={WIDTH}
      height={HEIGHT}
    />
    <Composition
      id="QL-Batch-Checkerboards"
      component={BatchCheckerboards}
      durationInFrames={pageConfigs.length}
      fps={1}
      width={WIDTH}
      height={HEIGHT}
    />
    {pageConfigs.map((page) => (
      <Folder key={page.page} name={page.page}>
        {page.layers.map((layer) => (
          <Still
            key={layer.id}
            id={layer.id}
            component={() => <TransparentEntry {...toLayerEntry(page, layer)} />}
            width={WIDTH}
            height={HEIGHT}
          />
        ))}
        <Still
          id={`${page.page}-Combined`}
          component={() => <TransparentEntry {...toCombinedEntry(page)} />}
          width={WIDTH}
          height={HEIGHT}
        />
        <Still
          id={`${page.page}-Checkerboard`}
          component={() => <CheckerboardEntry {...toCombinedEntry(page)} />}
          width={WIDTH}
          height={HEIGHT}
        />
      </Folder>
    ))}
  </>
);

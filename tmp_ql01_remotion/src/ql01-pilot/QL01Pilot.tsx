import {AbsoluteFill, CanvasImage, Still, staticFile} from "remotion";
import {featherRectMask, type Rect} from "./feather-mask";

const WIDTH = 1920;
const HEIGHT = 1080;
const FEATHER = 18;

const layers = [
  {
    id: "QL01-L01-Supply",
    rect: {x: 174, y: 238, width: 502, height: 412},
  },
  {
    id: "QL01-L02-Production",
    rect: {x: 672, y: 238, width: 561, height: 412},
  },
  {
    id: "QL01-L03-Sales",
    rect: {x: 1256, y: 238, width: 538, height: 412},
  },
  {
    id: "QL01-L04-Recycle",
    rect: {x: 174, y: 645, width: 778, height: 280},
  },
  {
    id: "QL01-L05-Summary",
    rect: {x: 947, y: 696, width: 793, height: 195},
  },
] as const satisfies readonly {readonly id: string; readonly rect: Rect}[];

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

const SourceWithMask: React.FC<{readonly rects: readonly Rect[]; readonly useNativeCrop: boolean}> = ({
  rects,
  useNativeCrop,
}) => {
  const nativeCrop = useNativeCrop && rects.length === 1 ? cropProps(rects[0]) : {};

  return (
    <CanvasImage
      src={staticFile("ql-01-pilot/ql-01-source.png")}
      style={{position: "absolute", left: 0, top: 0, width: WIDTH, height: HEIGHT}}
      effects={[featherRectMask({rects: flattenRects(rects), feather: FEATHER})]}
      {...nativeCrop}
    />
  );
};

const TransparentLayer: React.FC<{readonly rect: Rect}> = ({rect}) => (
  <AbsoluteFill style={{backgroundColor: "transparent"}}>
    <SourceWithMask rects={[rect]} useNativeCrop />
  </AbsoluteFill>
);

const Combined: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: "transparent"}}>
    <SourceWithMask rects={layers.map(({rect}) => rect)} useNativeCrop={false} />
  </AbsoluteFill>
);

const Checkerboard: React.FC = () => (
  <AbsoluteFill
    style={{
      backgroundColor: "#d9dee7",
      backgroundImage:
        "linear-gradient(45deg, #f6f7f9 25%, transparent 25%), linear-gradient(-45deg, #f6f7f9 25%, transparent 25%), linear-gradient(45deg, transparent 75%, #f6f7f9 75%), linear-gradient(-45deg, transparent 75%, #f6f7f9 75%)",
      backgroundPosition: "0 0, 0 24px, 24px -24px, -24px 0px",
      backgroundSize: "48px 48px",
    }}
  >
    <SourceWithMask rects={layers.map(({rect}) => rect)} useNativeCrop={false} />
  </AbsoluteFill>
);

export const QL01PilotStills: React.FC = () => (
  <>
    {layers.map(({id, rect}) => (
      <Still
        key={id}
        id={id}
        component={() => <TransparentLayer rect={rect} />}
        width={WIDTH}
        height={HEIGHT}
      />
    ))}
    <Still id="QL01-Combined" component={Combined} width={WIDTH} height={HEIGHT} />
    <Still id="QL01-Checkerboard" component={Checkerboard} width={WIDTH} height={HEIGHT} />
  </>
);

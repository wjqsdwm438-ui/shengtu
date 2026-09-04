import {createEffect, type InteractivitySchema} from "remotion";

export type Rect = {
  readonly x: number;
  readonly y: number;
  readonly width: number;
  readonly height: number;
};

type FeatherMaskParams = {
  readonly rects?: readonly number[];
  readonly feather?: number;
  readonly feathers?: readonly number[];
};

const schema = {
  rects: {
    type: "array",
    item: {
      type: "number",
      min: 0,
      max: 1920,
      step: 1,
    },
    default: [],
    minLength: 4,
    maxLength: 80,
    newItemDefault: 0,
    description: "Flattened rectangles: x, y, width, height",
    keyframable: false,
  },
  feather: {
    type: "number",
    min: 1,
    max: 80,
    step: 1,
    default: 18,
    description: "Inner alpha feather in pixels",
    hiddenFromList: false,
  },
  feathers: {
    type: "array",
    item: {
      type: "number",
      min: 1,
      max: 80,
      step: 1,
    },
    default: [],
    minLength: 0,
    maxLength: 20,
    newItemDefault: 18,
    description: "Optional per-rectangle feather values",
    keyframable: false,
  },
} as const satisfies InteractivitySchema;

const resolve = (params: FeatherMaskParams) => ({
  rects: params.rects ?? [],
  feather: params.feather ?? 18,
  feathers: params.feathers ?? [],
});

const smoothstep = (value: number) => value * value * (3 - 2 * value);

export const featherRectMask = createEffect<FeatherMaskParams, null>({
  type: "cn.shengtu.ql01.featherRectMask",
  label: "featherRectMask()",
  documentationLink: null,
  backend: "2d",
  calculateKey: (params) => {
    const {rects, feather, feathers} = resolve(params);
    return `ql01-feather-${feather}-${feathers.join("-")}-${rects.join("-")}`;
  },
  setup: () => null,
  apply: ({source, target, width, height, params}) => {
    const ctx = target.getContext("2d", {willReadFrequently: true});
    if (!ctx) {
      throw new Error("Could not get a 2D context for featherRectMask().");
    }

    const {rects: flatRects, feather, feathers} = resolve(params);
    const rects: Array<Rect & {readonly feather: number}> = [];
    for (let index = 0; index < flatRects.length; index += 4) {
      const rectIndex = index / 4;
      rects.push({
        x: flatRects[index],
        y: flatRects[index + 1],
        width: flatRects[index + 2],
        height: flatRects[index + 3],
        feather: feathers[rectIndex] ?? feather,
      });
    }

    ctx.clearRect(0, 0, width, height);
    ctx.globalCompositeOperation = "source-over";
    ctx.globalAlpha = 1;
    ctx.filter = "none";
    ctx.drawImage(source, 0, 0, width, height);

    const image = ctx.getImageData(0, 0, width, height);
    const data = image.data;

    for (let y = 0; y < height; y++) {
      const py = y + 0.5;
      for (let x = 0; x < width; x++) {
        const px = x + 0.5;
        let unionAlpha = 0;

        for (const rect of rects) {
          const right = rect.x + rect.width;
          const bottom = rect.y + rect.height;
          if (px < rect.x || px > right || py < rect.y || py > bottom) {
            continue;
          }

          const edgeDistance = Math.min(
            px - rect.x,
            right - px,
            py - rect.y,
            bottom - py,
          );
          const normalized = Math.max(0, Math.min(1, edgeDistance / rect.feather));
          unionAlpha = Math.max(unionAlpha, smoothstep(normalized));
          if (unionAlpha === 1) {
            break;
          }
        }

        const alphaIndex = (y * width + x) * 4 + 3;
        data[alphaIndex] = Math.round(data[alphaIndex] * unionAlpha);
      }
    }

    ctx.clearRect(0, 0, width, height);
    ctx.putImageData(image, 0, 0);
    ctx.globalCompositeOperation = "source-over";
    ctx.globalAlpha = 1;
    ctx.filter = "none";
  },
  cleanup: () => undefined,
  schema,
  validateParams: ({rects = [], feather = 18, feathers = []}) => {
    if (!Array.isArray(rects) || rects.length === 0 || rects.length % 4 !== 0) {
      throw new TypeError("rects must contain x, y, width, height groups.");
    }
    if (rects.some((value) => typeof value !== "number" || !Number.isFinite(value))) {
      throw new TypeError("Every rect value must be a finite number.");
    }
    if (typeof feather !== "number" || !Number.isFinite(feather) || feather <= 0) {
      throw new TypeError("feather must be a positive finite number.");
    }
    if (!Array.isArray(feathers) || feathers.some((value) => typeof value !== "number" || !Number.isFinite(value) || value <= 0)) {
      throw new TypeError("Every per-rectangle feather must be a positive finite number.");
    }
    if (feathers.length > 0 && feathers.length !== rects.length / 4) {
      throw new TypeError("feathers must be empty or match the rectangle count.");
    }
  },
});

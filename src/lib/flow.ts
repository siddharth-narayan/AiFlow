import { writable, type Writable } from "svelte/store";
import type {
    DataType,
    ModelInputType,
    ModelOutputType,
    ModelType,
} from "./api/triton/types";

export let inputs: Writable<{ name: string; data_type: DataType }[]> = writable(
    [],
);
export let outputs: Writable<{ name: string; data_type: DataType }[]> =
    writable([]);

let addModelCallback: (model: ModelType) => void;
export function regsiterAddModelCallback(func: (model: ModelType) => void) {
    addModelCallback = func;
}

export function addModel(model: ModelType) {
    addModelCallback(model);
}

export type ModelNodeType = {
    id: string,
    type: "modelNode",
    position: { x: number, y: number},
    data: ModelType
}

export type InputNodeType = {
    id: string,
    type: "modelNode",
    position: { x: number, y: number},
    data: ModelType
}

export type OutputNodeType = {
    id: string,
    type: "outputNode",
    position: { x: number, y: number},
    data: ModelType
}
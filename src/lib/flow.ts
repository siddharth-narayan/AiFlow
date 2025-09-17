import { writable, type Writable } from "svelte/store";
import type {
    DataType,
    ModelInputType,
    ModelOutputType,
    ModelType,
} from "./api/triton/types";
import type { NodeTypes } from "@xyflow/svelte";

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


export type AnyNodeType = ModelNodeType | InputNodeType | OutputNodeType

export type ModelNodeType = NodeTypes & {
    id: string,
    type: "modelNode",
    data: ModelType
}

export type InputNodeType = NodeTypes & {
    id: string,
    type: "inputNode",
    data: ModelInputType[]
}

export type OutputNodeType = NodeTypes & {
    id: string,
    type: "outputNode",
    data: ModelOutputType[]
}
import { writable, type Writable } from "svelte/store";
import type {
    DataType,
    ModelInputType,
    ModelOutputType,
    ModelType,
} from "./api/triton/types";
import type { Edge, EdgeTypes, Node, NodeTypes } from "@xyflow/svelte";

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

export function getNodeFromId(nodes: AnyNodeType[], id: string) {
    return nodes.find((node) => {
        return node.id == id;
    });
}

export type AnyNodeType = ModelNodeType | InputNodeType | OutputNodeType

export type ModelNodeType = Node & {
    type: "modelNode",
    data: ModelType
}

export type InputNodeType = Node & {
    type: "inputNode",
    // data: ModelInputType[]
}

export type OutputNodeType = Node & {
    type: "outputNode",
    // data: ModelOutputType[]
}
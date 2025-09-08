import { writable, type Writable } from "svelte/store";
import type { DataType, ModelInputType, ModelOutputType, ModelType } from "./api/triton/types";

export let inputs: Writable<{name: string, data_type: DataType}[]> = writable([])
export let outputs: Writable<{name: string, data_type: DataType}[]> = writable([])

// Returns a css string percentage to style the correct position on a handle
export  function customHandlePosition(index: number, count: number) {
    let globalPosition = 50; // The placement of the center of all the handles
    let handleHeight = 70; // Total height (percentage) of all the handles

    let distance = handleHeight / count;

    // Minimum 10% distance
    distance = distance < 10 ? 10 : distance;

    let firstHandlePosition = globalPosition - ((count - 1) * distance) / 2;
    // Position of the specific handle
    let position = firstHandlePosition + index * distance;

    return `top:${position}%;`;
  }

  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < i; j++) {
      console.log(
        `index: ${j} count: ${i} position: ${customHandlePosition(j, i)}`,
      );
    }
  }

  let addModelCallback: (model: ModelType) => void
  export function regsiterAddModelCallback(func: (model: ModelType) => void) {
    addModelCallback = func
  }

  export function addModel(model: ModelType) {
    addModelCallback(model)
  }

  export enum FlowElementType {
    Model,
    Input,
    Output,
    Tokenizer
  }

  export enum FlowNodeType {
    Model,
    Tokenizer
  }
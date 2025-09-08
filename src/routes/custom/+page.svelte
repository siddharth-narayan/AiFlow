<script lang="ts">
  import { v4 } from "uuid";
  import { triton } from "$lib/api/triton/api";
  import type { ModelType } from "$lib/api/triton/types";
  import Flow from "$lib/components/large/flow/flow.svelte";
  import { regsiterAddModelCallback } from "$lib/flow";

  // Things to improve on the flow
  // Don't allow deletion of input/output nodes
  // Allow deletion of lines without deleting nodes
  // Allow removing input/outputs
  async function submit() {}

  // Svelte Flow stuff
  let nodes: {
    id: string;
    type: string;
    position: { x: number; y: number };
    data: any;
  }[] = $state([]);

  function addModel(model: ModelType) {
    nodes.push({
      id: v4(),
      type: "model",
      position: { x: 50, y: 50 },
      data: model,
    });
  }

  regsiterAddModelCallback(addModel);

  // If I don't keep the triton.ready wrapper stuff breaks, probably because of something in how svelte manages state.
  // I don't want to deal with it so it's going to stay like this for now
  triton.ready.then(() => {
    triton.models;

    nodes = [];
    nodes.push(
      {
        id: "input",
        type: "inputNode",
        position: { x: 200, y: 200 },
        data: {
          inputs: [],
        },
      },
      {
        id: "output",
        type: "outputNode",
        position: { x: 500, y: 200 },
        data: {
          inputs: [],
        },
      },
    );
  });

  let edges = $state([]);
</script>

<Flow bind:edges bind:nodes />

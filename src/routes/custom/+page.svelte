<script lang="ts">
  import { v4 } from "uuid";
  import { triton } from "$lib/api/triton/api";
  import type { ModelType } from "$lib/api/triton/types";
  import Flow from "$lib/components/large/flow/flow.svelte";
  import { inputs, regsiterAddModelCallback } from "$lib/flow";
  import { GripVertical } from "lucide-svelte/icons";
  import { PaneGroup, Pane, PaneResizer } from "paneforge";
  import AiMediaInput from "$lib/components/large/ai-media-input.svelte";
  import { GripHorizontal } from "@lucide/svelte";

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

<PaneGroup direction="vertical" class="flex flex-col gap-8 p-4">
  <Pane>
    <PaneGroup
      direction="horizontal"
      class="flex gap-8 p-4"
      style="height: auto;"
    >
      {#each $inputs as input, index}
        <Pane defaultSize={50}>
          <label class="text-secondary-foreground flex flex-col gap-2">
            <h1>{input.name}</h1>
            <AiMediaInput value="" type={input}></AiMediaInput>
          </label>
        </Pane>

        {#if index != $inputs.length - 1}
          <PaneResizer class="bg-accent w-0.5 content-center center"
            ><GripVertical></GripVertical></PaneResizer
          >
        {/if}
      {/each}
      <!-- <Pane defaultSize={50}>

  </Pane>
	
	<Pane defaultSize={50}>Pane 2</Pane> -->
    </PaneGroup>
  </Pane>
  <PaneResizer class="flex bg-accent h-0.5 items-center justify-center"
    ><GripHorizontal></GripHorizontal></PaneResizer
  >
  <Pane>
    <Flow bind:edges bind:nodes />
  </Pane>
</PaneGroup>

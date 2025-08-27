<script lang="ts">
  import { triton } from "$lib/api/triton/api";
  import Loader2Icon from "@lucide/svelte/icons/loader-2";
  import AiMediaInput from "$lib/components/large/ai-media-input.svelte";
  import AiMediaOutput from "$lib/components/large/ai-media-output.svelte";
  import SingleSelect from "$lib/components/large/single-select.svelte";
  import { Button } from "$lib/components/ui/button";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import { Separator } from "$lib/components/ui/separator/index.js";

  import { mode } from "mode-watcher";
  import {
    Controls,
    MiniMap,
    SvelteFlow,
    Background,
    Position,
    type ColorMode,
    Panel,
  } from "@xyflow/svelte";
  import "@xyflow/svelte/dist/style.css";
  import ModelNode from "$lib/components/large/flow/model-node.svelte";
  import { Plus } from "@lucide/svelte";

  let media_type_1 = $state("text");
  let media_type_2 = $state("text");

  let selectedModel = $state("");

  let mediaTypes = ["text", "audio", "video", "3D"];

  let inputValue = $state("");
  let outputValue = $state("");

  let loading = $state(false);

  async function submit() {
    let inputs = [
      {
        name: "text_input",
        shape: [1],
        datatype: "BYTES",
        data: [inputValue],
      },
    ];

    let outputs = [{ name: "text_output" }];

    loading = true;
    let resp = await triton.infer(selectedModel, inputs, outputs);
    resp.json().then((json) => {
      loading = false;
      outputValue = json["outputs"][0]["data"][0];
    });
  }

  // Svelte Flow stuff
  let nodes: { id: string; position: { x: number; y: number }; data: any }[] =
    $state.raw([]);
  triton.ready.then(() => {
    triton.models;

    nodes = triton.models.map((model, index) => {
      return {
        id: index.toString(),
        type: "modelNode",
        position: { x: 0, y: index * 50 },
        data: model,
      };
    });

    console.log(nodes);
  });
  // [
  //   {
  //     id: "1",
  //     position: { x: 0, y: 0 },
  //     data: { label: "1" },
  //     sourcePosition: Position.Right,
  //     targetPosition: Position.Left,
  //   },
  //   {
  //     id: "2",
  //     position: { x: 0, y: 100 },
  //     data: { label: "2" },
  //     sourcePosition: Position.Right,
  //     targetPosition: Position.Left,
  //   },
  // ]

  let edges = $state.raw([{ id: "e1-2", source: "1", target: "2" }]);
</script>

<div class="flex justify-center items-center gap-4 p-4">
  {#await triton.filterModels(media_type_1, media_type_2) then models}
    <label>Model: </label>
    <SingleSelect
      bind:value={selectedModel}
      options={models.map((model) => model.name)}
    />
  {/await}
</div>
<Separator orientation="horizontal" />
<div class="flex gap-4 p-4 h-full">
  <div class="w-1/2 flex flex-col gap-4 items-center">
    <SingleSelect bind:value={media_type_1} options={mediaTypes}></SingleSelect>
    <AiMediaInput type={media_type_1} bind:value={inputValue} />
    <Button disabled={loading} onclick={submit}>
      {#if loading}
        <Loader2Icon class="animate-spin" />
      {/if}
      Submit
    </Button>
  </div>
  <Separator orientation="vertical" />
  <div class="w-1/2 flex flex-col gap-4 items-center">
    <SingleSelect bind:value={media_type_2} options={mediaTypes}></SingleSelect>
    <AiMediaOutput type={media_type_1} value={outputValue} />
  </div>
</div>

<SvelteFlow
  nodeTypes={{ modelNode: ModelNode }}
  bind:nodes
  bind:edges
  colorMode={mode.current}
>
  <Background />
  <MiniMap />
  <Controls />
  <Panel>
    <DropdownMenu.Root>
      <DropdownMenu.Trigger>
        {#snippet child({ props })}
          <Button {...props} variant="outline"><Plus />Add a Node</Button>
        {/snippet}
      </DropdownMenu.Trigger>
      <DropdownMenu.Content class="w-56" align="start">
        <DropdownMenu.Sub>
          <DropdownMenu.SubTrigger><Plus />Add Input</DropdownMenu.SubTrigger>
          <DropdownMenu.SubContent>
            {#await triton.ready then _}
              {#each triton.models as model}
                <DropdownMenu.Item>{model.name}</DropdownMenu.Item>
              {/each}
            {/await}
          </DropdownMenu.SubContent>
        </DropdownMenu.Sub>
        <DropdownMenu.Sub>
          <DropdownMenu.SubTrigger><Plus />Add Output</DropdownMenu.SubTrigger>
          <DropdownMenu.SubContent>
            {#await triton.ready then _}
              {#each triton.models as model}
                <DropdownMenu.Item>{model.name}</DropdownMenu.Item>
              {/each}
            {/await}
          </DropdownMenu.SubContent>
        </DropdownMenu.Sub>
        <DropdownMenu.Sub>
          <DropdownMenu.SubTrigger><Plus />Add Model</DropdownMenu.SubTrigger>
          <DropdownMenu.SubContent>
            {#await triton.ready then _}
              {#each triton.models as model}
                <DropdownMenu.Item>{model.name}</DropdownMenu.Item>
              {/each}
            {/await}
          </DropdownMenu.SubContent>
        </DropdownMenu.Sub>
      </DropdownMenu.Content>
    </DropdownMenu.Root>
  </Panel>
</SvelteFlow>

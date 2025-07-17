<script lang="ts">
  import { triton } from "$lib/api/triton/api";
  import AiMediaInput from "$lib/components/large/ai-media-input.svelte";
  import AiMediaOutput from "$lib/components/large/ai-media-output.svelte";
  import SingleSelect from "$lib/components/large/single-select.svelte";
  import { Button } from "$lib/components/ui/button";
  import {
    AutoTokenizer,
    InterruptableStoppingCriteria,
    TextStreamer,
  } from "@huggingface/transformers";
  import { Separator } from "$lib/components/ui/separator/index.js";

  // TODO: Move TritonApiInstance to shared between components

  let media_type_1 = $state("text");
  let media_type_2 = $state("text");

  let selectedModel = $state("");

  let mediaTypes = new Map();
  mediaTypes.set("audio", "BYTES");
  mediaTypes.set("video", "BYTES");
  mediaTypes.set("text", "TYPE_STRING");
  mediaTypes.set("3D", "BYTES");

  let outputValue = $state("");
  let inputValue = $state("");

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

    let resp = await triton.infer(selectedModel, inputs, outputs);
    resp.json().then((j) => {
      console.log(j)
      console.log(j["outputs"][0]["data"][0])
      outputValue = j["outputs"][0]["data"][0]
    })
  }
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
    <SingleSelect bind:value={media_type_1} options={mediaTypes.keys()}
    ></SingleSelect>
    <AiMediaInput type={media_type_1} bind:value={inputValue} />
    <Button onclick={submit}>Submit</Button>
  </div>
  <Separator orientation="vertical" />
  <div class="w-1/2 flex flex-col gap-4 items-center">
    <SingleSelect bind:value={media_type_2} options={mediaTypes.keys()}
    ></SingleSelect>
    <AiMediaOutput type={media_type_1} value={outputValue} />
  </div>
</div>

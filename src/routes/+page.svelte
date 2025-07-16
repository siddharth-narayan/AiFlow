<script lang="ts">
  import { triton } from "$lib/api/triton/api";
  import AiMediaInput from "$lib/components/large/ai-media-input.svelte";
  import AiMediaOutput from "$lib/components/large/ai-media-output.svelte";
  import SingleSelect from "$lib/components/large/single-select.svelte";
  import { Button } from "$lib/components/ui/button";

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

  function submit() {
    console.log("submit");
  }
</script>

<div class="flex justify-center items-center gap-4 p-4">

  {#await triton.filterModels(media_type_1, media_type_2) then models}
      <label>Model: </label>
      <SingleSelect
        value={selectedModel}
        options={models
          .map((model) => model.name)}
      />
  {/await}
</div>

<div class="flex gap-4 p-4 h-full">
  <div class="w-1/2 flex flex-col gap-4 items-center">
    <SingleSelect bind:value={media_type_1} options={mediaTypes.keys()}
    ></SingleSelect>
    <AiMediaInput type={media_type_1} />
    <Button onclick={submit}>Submitshs</Button>
  </div>
  <Separator orientation="vertical" />
  <div class="w-1/2 flex flex-col gap-4 items-center">
    <SingleSelect bind:value={media_type_2} options={mediaTypes.keys()}
    ></SingleSelect>
    <AiMediaOutput type={media_type_1} />
  </div>
</div>

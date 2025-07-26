<script lang="ts">
  import { triton } from "$lib/api/triton/api";
  import Loader2Icon from "@lucide/svelte/icons/loader-2";
  import AiMediaInput from "$lib/components/large/ai-media-input.svelte";
  import AiMediaOutput from "$lib/components/large/ai-media-output.svelte";
  import SingleSelect from "$lib/components/large/single-select.svelte";
  import { Button } from "$lib/components/ui/button";
  import { Separator } from "$lib/components/ui/separator/index.js";
  import { z } from "zod"
  import ZxForm from "zxforms-svelte";

  let schema = z.object({
    tritonEndpoint: z.string().url()
  })

</script>

<ZxForm {schema}></ZxForm>
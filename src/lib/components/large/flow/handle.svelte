<script lang="ts">
    import type { ModelInputType, ModelOutputType } from "$lib/api/triton/types";
    import type { ModelOutput } from "@huggingface/transformers";
    import { Handle, Position } from "@xyflow/svelte";

    type Props = {
        handleIO: ModelInputType | ModelOutputType,
        handleIndex: number,
        handleTotal: number,
    }

    let { input, output, handleIndex, handleTotal  : Props} = $props();

    let left = !input ? false : true
    if (!input && !output) {

    }
    // Returns a css string percentage to style the correct position on a handle
    export function customHandlePosition(index: number, count: number) {
        let globalPosition = 50; // The placement of the center of all the handles
        let handleHeight = 70; // Total height (percentage) of all the handles

        let distance = handleHeight / count;

        // Minimum 10% distance
        distance = distance < 30 ? 30 : distance;

        let firstHandlePosition = globalPosition - ((count - 1) * distance) / 2;
        // Position of the specific handle
        let position = firstHandlePosition + index * distance;

        return `top:${position}%;`;
    }
</script>

<Handle
    class="w-2"
    id={input.name}
    type="target"
    position={Position.Left}
    style={customHandlePosition(handleIndex, handleTotal)}
/>

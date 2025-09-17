<script lang="ts">
    import type {
        ModelInputType,
        ModelOutputType,
    } from "$lib/api/triton/types";
    import { Handle, Position } from "@xyflow/svelte";
    import { v4 as uuid } from "uuid";

    type Props = {
        handleIO: ModelInputType | ModelOutputType;
        handleIndex: number;
        handleTotal: number;
        position: Position;
        type?: "source" | "target" // Or both if that exists? 
    };

    let { handleIO, handleIndex, handleTotal, position, type }: Props = $props();

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
    id={uuid()}
    type="target"
    {position}
    style={customHandlePosition(handleIndex, handleTotal)}
/>

{#if position == Position.Left}
    <div
        class="left-edge-label"
        style={customHandlePosition(handleIndex, handleTotal)}
    >
        <p class="font-bold">{handleIO.name}</p>
        <p class="font-bold text-sm text-muted-foreground">
            {handleIO.data_type}
        </p>

        <!-- <p>{input.data_type} with dimension(s) [{input.dims.toString()}]</p> -->
    </div>
{:else if position == Position.Right}
    <div
        class="right-edge-label"
        style={customHandlePosition(handleIndex, handleTotal)}
    >
        
        <p class="font-bold">{handleIO.name}</p>
        <p>{handleIO.name}</p>
        <p class="font-bold text-sm text-muted-foreground">
            {handleIO.data_type}
        </p>

        <!-- <p>{input.data_type} with dimension(s) [{input.dims.toString()}]</p> -->
    </div>
{/if}

<style>
    .left-edge-label {
        position: absolute;
        left: 0;
        transform: translateX(calc(-100% - 0.5rem)) translateY(-50%);
    }

    .right-edge-label {
        position: absolute;
        right: 0;
        transform: translateX(calc(100% + 0.5rem)) translateY(-50%);
    }
</style>

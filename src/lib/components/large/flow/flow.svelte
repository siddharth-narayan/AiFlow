<script lang="ts">
    import {
        Background,
        Controls,
        MiniMap,
        Panel,
        SvelteFlow,
        type Connection,
    } from "@xyflow/svelte";
    import ModelNode from "./model-node.svelte";
    import { mode } from "mode-watcher";
    import "@xyflow/svelte/dist/style.css";
    import InputNode from "./input-node.svelte";
    import AddPanel from "./add-panel.svelte";
    import OutputNode from "./output-node.svelte";
    import { LoaderCircle } from "@lucide/svelte";
    import type { ModelType } from "$lib/api/triton/types";
    import { Play } from "lucide-svelte";
    import Button from "$lib/components/ui/button/button.svelte";
    import type { AnyNodeType } from "$lib/flow";

    let {
        nodes = $bindable(),
        edges = $bindable(),
    }: { nodes: AnyNodeType[]; edges: any } = $props();

    function validateConnection(connection: Connection) {
        let finalSourceType = "";
        let finalTargetType = "";

        let source: AnyNodeType | undefined = nodes.find((node) => {
            return node.id == connection.source;
        });

        let target: AnyNodeType | undefined = nodes.find((node) => {
            return node.id == connection.target;
        });

        if (!source || !target) {
            return false;
        }
        
        // Special cases for beginning and ending nodes, because they don't have a (source/target).data
        // source.type can never be "outputNode", but it's included to stop type errors
        if (source.type == "inputNode" || source.type == "outputNode") {
            return false;
            if (!connection.sourceHandle) {
                return connection;
            }

            finalSourceType = "";
        }
        if (target.type == "outputNode" || target.type == "inputNode") {
            return false;
            if (!connection.targetHandle) {
                return connection;
            }

            finalSourceType = "";
        }
        let sourceInput = source.data.output.find((output) => {
            console.log(`"${connection.sourceHandle}"`)
            return output.name == connection.sourceHandle;
        });

        let targetInput = target.data.input.find((input) => {
            return input.name == connection.targetHandle;
        });

        if (!sourceInput || !targetInput) {
            return false
        }

        finalSourceType = sourceInput.data_type
        finalTargetType = targetInput.data_type;

        console.log(finalSourceType)
        console.log(finalTargetType)
        // Should add validation here for dimensionality as well

        return finalSourceType === finalTargetType ? connection : false;
    }

    let running = $state(false);

    function start() {
        running = true;
        setTimeout(() => {
            running = false;
        }, 10000);
        console.log("HAHE");
    }
</script>

<SvelteFlow
    nodeTypes={{
        modelNode: ModelNode,
        inputNode: InputNode,
        outputNode: OutputNode,
    }}
    bind:nodes
    bind:edges
    onbeforeconnect={validateConnection}
    colorMode={mode.current}
>
    <!--  onbeforeconnect={validateConnection} -->
    <Background />
    <!-- <MiniMap /> -->
    <Controls />
    <AddPanel />
    <Panel position="bottom-right">
        {#if !running}
            <Button onclick={start} variant="constructive"
                >Start <Play /></Button
            >
        {:else}
            <Button variant="secondary" disabled
                >Running <LoaderCircle class="animate-spin" /></Button
            >
        {/if}
    </Panel>
</SvelteFlow>

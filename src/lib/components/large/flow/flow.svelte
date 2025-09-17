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

        console.log("Validating connection");
        let source: AnyNodeType | undefined = nodes.find((node) => {
            return node.id == connection.source;
        });

        let target = nodes.find((node) => {
            return node.id == connection.target;
        });

        if (!source || !target) {
            return false;
        }

        // Special cases for beginning and ending nodes, because they don't have a (source/target).data
        if (source.type == "inputNode") {
            if (!connection.sourceHandle) {
                return connection;
            }

            finalSourceType = "";
        }

        if (source.type == "outputNode") {
            if (!connection.targetHandle) {
                return connection;
            }

            finalSourceType = "";
        }

        console.log(source);
        console.log(source.data);
        let sourceInput = (source.data as ModelType).input.find((input) => {
            input.name == connection.sourceHandle;
        });

        console.log(target.data);
        let targetInput = (target.data as ModelType).input.find((input) => {
            input.name == connection.sourceHandle;
        });

        console.log(sourceInput);

        return connection;
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

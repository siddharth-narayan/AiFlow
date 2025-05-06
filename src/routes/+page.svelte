<script lang="ts">
    import { Button } from "$lib/components/ui/button";
    import { Sidebar, SidebarContent, SidebarFooter, SidebarGroup, SidebarHeader, SidebarProvider, SidebarTrigger } from "$lib/components/ui/sidebar";
    import Moon from "@lucide/svelte/icons/moon";
    import Sun from "@lucide/svelte/icons/sun";
    import { toggleMode } from "mode-watcher";

    let { children } = $props();
</script>
<div class="flex felx-row p-4">
<SidebarProvider>
    <Sidebar>
        <SidebarHeader></SidebarHeader>
        <SidebarContent>
            <SidebarGroup></SidebarGroup>
        </SidebarContent>
        <SidebarFooter></SidebarFooter>
    </Sidebar>
    <main>
        <SidebarTrigger />
        {@render children?.()}
    </main>
</SidebarProvider>
<div>
<Button onclick={toggleMode} variant="outline" size="icon">
	<Sun
	  class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
	/>
	<Moon
	  class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100"
	/>
	<span class="sr-only">Toggle theme</span>
</Button>
</div>
</div>
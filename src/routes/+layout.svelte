<script lang="ts">
	import "../app.css";

	import {
		Sidebar,
		SidebarContent,
		SidebarFooter,
		SidebarGroup,
		SidebarHeader,
		SidebarProvider,
		SidebarTrigger,
	} from "$lib/components/ui/sidebar";
	import { ModeWatcher } from "mode-watcher";
	import ThemeSwitcher from "$lib/components/theme-switcher.svelte";

	let { children } = $props();
</script>

<ModeWatcher />

<div class="flex gap-4">
	<SidebarProvider style="--sidebar-width: 20rem;">
		<Sidebar>
			<SidebarHeader></SidebarHeader>
			<SidebarContent>
				<SidebarGroup></SidebarGroup>
			</SidebarContent>
			<SidebarFooter>
				<ThemeSwitcher />
			</SidebarFooter>
		</Sidebar>
		<SidebarTrigger />
	</SidebarProvider>

	<div class="w-full">
		{@render children()}
	</div>
</div>

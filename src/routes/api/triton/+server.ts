// src/routes/api/[...path]/+server.ts
import type { RequestHandler } from './$types';

async function proxyTriton ({ params, request }) {
	const proxiedUrl = `http://localhost:4000/api/${params.path}`;
	const res = await fetch(proxiedUrl, {
		method: request.method,
		headers: {
			// Forward headers if needed
			...Object.fromEntries(request.headers)
		}
	});

	const data = await res.text(); // or res.json() depending on the API
	return new Response(data, {
		status: res.status,
		headers: {
			'Content-Type': res.headers.get('content-type') || 'text/plain'
		}
	});
};

export const GET = proxyTriton
export const POST = proxyTriton
// Cloudflare Pages Function to serve a standard robots.txt
// This bypasses the Cloudflare AI Audit feature that replaces robots.txt with Content-Signal protocol.
// Pages Functions run at the edge BEFORE the AI Audit middleware, so this correctly returns a
// standard robots.txt that Googlebot can understand.

export async function onRequest(context) {
  const robots = `User-agent: *
Allow: /
Sitemap: https://game-guide.club/sitemap.xml

# Allow Googlebot fully
User-agent: Googlebot
Allow: /

# Allow Googlebot-News
User-agent: Googlebot-News
Allow: /
`;

  return new Response(robots, {
    headers: {
      'Content-Type': 'text/plain',
      'Cache-Control': 'public, max-age=86400'
    }
  });
}

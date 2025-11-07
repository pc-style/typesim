import { DocsLayout } from '@/components/docs-layout';
import { notFound } from 'next/navigation';

const docsMap: Record<string, () => Promise<any>> = {
  'getting-started': () => import('@/content/docs/getting-started.mdx'),
  'installation': () => import('@/content/docs/installation.mdx'),
  'configuration': () => import('@/content/docs/configuration.mdx'),
  'usage': () => import('@/content/docs/usage.mdx'),
  'api': () => import('@/content/docs/api.mdx'),
  'examples': () => import('@/content/docs/examples.mdx'),
};

export async function generateStaticParams() {
  return Object.keys(docsMap).map((slug) => ({
    slug: [slug],
  }));
}

export default async function DocsPage({
  params,
}: {
  params: Promise<{ slug: string[] }>;
}) {
  const { slug } = await params;
  const docSlug = slug?.[0] || 'getting-started';

  if (!docsMap[docSlug]) {
    notFound();
  }

  try {
    const DocContent = (await docsMap[docSlug]()).default;

    return (
      <DocsLayout>
        <article className="prose prose-lg max-w-none dark:prose-invert">
          <DocContent />
        </article>
      </DocsLayout>
    );
  } catch (error) {
    console.error('Error loading doc:', error);
    notFound();
  }
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string[] }>;
}) {
  const { slug } = await params;
  const docSlug = slug?.[0] || 'getting-started';

  const titles: Record<string, string> = {
    'getting-started': 'Getting Started',
    'installation': 'Installation',
    'configuration': 'Configuration',
    'usage': 'Usage',
    'api': 'API Reference',
    'examples': 'Examples',
  };

  return {
    title: `${titles[docSlug] || 'Documentation'} - typesim`,
    description: `typesim documentation - ${titles[docSlug] || 'Documentation'}`,
  };
}


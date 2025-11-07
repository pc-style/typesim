import { DocsLayout } from '@/components/docs-layout';
import Link from 'next/link';
import { Button } from '@/components/ui/button';

export default function NotFound() {
  return (
    <DocsLayout>
      <div className="text-center py-20">
        <h1 className="text-4xl font-bold mb-4">404</h1>
        <p className="text-xl text-muted-foreground mb-8">
          Documentation page not found
        </p>
        <Link href="/docs/getting-started">
          <Button>Go to Getting Started</Button>
        </Link>
      </div>
    </DocsLayout>
  );
}


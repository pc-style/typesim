import type { MDXComponents } from 'mdx/types';
import { CodeBlock } from '@/components/code-block';
import { Terminal } from '@/components/terminal';

export function useMDXComponents(components: MDXComponents): MDXComponents {
  return {
    code: ({ children, className, ...props }) => {
      const match = /language-(\w+)/.exec(className || '');
      const language = match ? match[1] : '';
      const isInline = !className;
      
      if (isInline) {
        return <code className="bg-muted px-1.5 py-0.5 rounded text-sm" {...props}>{children}</code>;
      }
      
      return <CodeBlock language={language} code={String(children).replace(/\n$/, '')} />;
    },
    pre: ({ children, ...props }) => {
      return <>{children}</>;
    },
    h1: ({ children }) => <h1 className="text-4xl font-bold mb-6 mt-8">{children}</h1>,
    h2: ({ children }) => <h2 className="text-3xl font-bold mb-4 mt-8 border-b-2 border-foreground pb-2">{children}</h2>,
    h3: ({ children }) => <h3 className="text-2xl font-bold mb-3 mt-6">{children}</h3>,
    h4: ({ children }) => <h4 className="text-xl font-bold mb-2 mt-4">{children}</h4>,
    p: ({ children }) => <p className="mb-4 leading-relaxed">{children}</p>,
    ul: ({ children }) => <ul className="list-disc list-inside mb-4 space-y-2">{children}</ul>,
    ol: ({ children }) => <ol className="list-decimal list-inside mb-4 space-y-2">{children}</ol>,
    li: ({ children }) => <li className="ml-4">{children}</li>,
    blockquote: ({ children }) => (
      <blockquote className="border-l-4 border-primary pl-4 italic my-4">{children}</blockquote>
    ),
    a: ({ href, children }) => (
      <a href={href} className="text-primary underline hover:text-primary/80">{children}</a>
    ),
    ...components,
  };
}


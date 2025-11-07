'use client';

import { useState } from 'react';

interface CodeBlockProps {
  code: string;
  language?: string;
  filename?: string;
}

export function CodeBlock({ code, language = 'text', filename }: CodeBlockProps) {
  const [copied, setCopied] = useState(false);

  const copyToClipboard = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="rounded-lg border bg-card my-4 shadow-lg overflow-hidden">
      {filename && (
        <div className="border-b px-4 py-2 bg-muted font-mono text-sm">
          {filename}
        </div>
      )}
      <div className="relative">
        <pre className="p-4 overflow-x-auto">
          <code className={`language-${language}`}>{code}</code>
        </pre>
        <button
          onClick={copyToClipboard}
          className="absolute top-2 right-2 px-3 py-1 rounded-md bg-primary text-primary-foreground text-xs font-semibold hover:opacity-80 transition-all shadow-md hover:shadow-lg"
        >
          {copied ? 'Copied!' : 'Copy'}
        </button>
      </div>
    </div>
  );
}


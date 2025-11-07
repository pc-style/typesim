'use client';

interface TerminalProps {
  command: string;
  output?: string;
}

export function Terminal({ command, output }: TerminalProps) {
  return (
    <div className="neo-border bg-black text-green-400 font-mono text-sm my-4">
      <div className="border-b-2 border-green-400 px-4 py-2 bg-gray-900">
        <span className="text-green-400">$</span>
      </div>
      <div className="p-4">
        <div className="text-white mb-2">
          <span className="text-green-400">$</span> {command}
        </div>
        {output && (
          <div className="text-green-400 whitespace-pre-wrap">{output}</div>
        )}
      </div>
    </div>
  );
}


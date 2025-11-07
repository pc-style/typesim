'use client';

interface TerminalProps {
  command: string;
  output?: string;
}

export function Terminal({ command, output }: TerminalProps) {
  // Process output to add color classes
  const processOutput = (text: string) => {
    const lines = text.split('\n');
    return lines.map((line, i) => {
      // Headers (like "typesim", "settings")
      if (line.trim().match(/^[a-z]+$/)) {
        return <div key={i} className="text-cyan-400 font-bold">{line}</div>;
      }
      // Separator lines
      if (line.includes('───')) {
        return <div key={i} className="text-gray-600">{line}</div>;
      }
      // Credits/footer
      if (line.includes('made by')) {
        return <div key={i} className="text-gray-600">{line}</div>;
      }
      // Menu prompts
      if (line.includes('[?]')) {
        return <div key={i} className="text-cyan-400">{line}</div>;
      }
      // Selected menu item
      if (line.trim().startsWith('>')) {
        return <div key={i} className="text-cyan-400">{line}</div>;
      }
      // Settings labels with values
      if (line.includes('probability') || line.includes('delay') || line.includes('pause') || 
          line.includes('use ai') || line.includes('countdown') || line.includes('speed')) {
        const parts = line.split(/(\d+\.?\d*%?|\d+-\d+ms|yes|no|\d+s|\d+\.?\d*x)/);
        return (
          <div key={i}>
            {parts.map((part, j) => {
              if (part.match(/\d+\.?\d*%?|\d+-\d+ms|yes|no|\d+s|\d+\.?\d*x/)) {
                return <span key={j} className="text-yellow-400">{part}</span>;
              }
              return <span key={j} className="text-gray-400">{part}</span>;
            })}
          </div>
        );
      }
      // Menu items
      if (line.trim() && !line.startsWith(' >')) {
        return <div key={i} className="text-gray-300">{line}</div>;
      }
      // Default/empty lines
      return <div key={i} className="text-gray-400">{line}</div>;
    });
  };

  return (
    <div className="rounded-lg border border-primary/20 bg-[#1a1625] font-mono text-sm my-4 shadow-lg shadow-primary/10 overflow-hidden">
      <div className="border-b border-primary/30 px-4 py-2 bg-[#0f0a1a]">
        <span className="text-primary">$</span>
      </div>
      <div className="p-4">
        <div className="text-white mb-3">
          <span className="text-primary">$</span> {command}
        </div>
        {output && (
          <div className="leading-relaxed">{processOutput(output)}</div>
        )}
      </div>
    </div>
  );
}


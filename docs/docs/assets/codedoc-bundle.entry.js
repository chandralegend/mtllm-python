import { getRenderer } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/transport/renderer.js';
import { initJssCs } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/transport/setup-jss.js';initJssCs();
import { installTheme } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/content/theme.ts';installTheme();
import { codeSelection } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/code/selection.js';codeSelection();
import { sameLineLengthInCodes } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/code/same-line-length.js';sameLineLengthInCodes();
import { initHintBox } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/code/line-hint/index.js';initHintBox();
import { initCodeLineRef } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/code/line-ref/index.js';initCodeLineRef();
import { initSmartCopy } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/code/smart-copy.js';initSmartCopy();
import { copyHeadings } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/heading/copy-headings.js';copyHeadings();
import { contentNavHighlight } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/page/contentnav/highlight.js';contentNavHighlight();
import { loadDeferredIFrames } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/transport/deferred-iframe.js';loadDeferredIFrames();
import { smoothLoading } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/transport/smooth-loading.js';smoothLoading();
import { tocHighlight } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/page/toc/toc-highlight.js';tocHighlight();
import { postNavSearch } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/page/toc/search/post-nav/index.js';postNavSearch();
import { copyLineLinks } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/code/line-links/copy-line-link.js';copyLineLinks();
import { gatherFootnotes } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/footnote/gather-footnotes.js';gatherFootnotes();
import { reloadOnChange } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/serve/reload.js';reloadOnChange();
import { ToCPrevNext } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/page/toc/prevnext/index.js';
import { GithubSearch } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/misc/github/search.js';
import { ToCToggle } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/page/toc/toggle/index.js';
import { DarkModeSwitch } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/darkmode/index.js';
import { ConfigTransport } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/transport/config.js';
import { TabSelector } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/tabs/selector.js';
import { CollapseControl } from '/Users/chandralegend/Desktop/Projects/mtllm-python/docs/.codedoc/node_modules/@codedoc/core/dist/es6/components/collapse/collapse-control.js';

const components = {
  'f0bkXQOosAj+idY9+sImag==': ToCPrevNext,
  '/Y+P1tYksWBwmcMlD2xXgw==': GithubSearch,
  '6TsxTa1ofWRNL2IqRhtHJA==': ToCToggle,
  'D7zjdQsfpPVXwI3O5t9Rbw==': DarkModeSwitch,
  '0Zm/UWd0bJKHysqxs9Wg6g==': ConfigTransport,
  'HZsOMHbNDMLc640zEU0drA==': TabSelector,
  '+iriQnW50EXSooCLiKrctw==': CollapseControl
};

const renderer = getRenderer();
const ogtransport = window.__sdh_transport;
window.__sdh_transport = function(id, hash, props) {
  if (hash in components) {
    const target = document.getElementById(id);
    renderer.render(renderer.create(components[hash], props)).after(target);
    target.remove();
  }
  else if (ogtransport) ogtransport(id, hash, props);
}

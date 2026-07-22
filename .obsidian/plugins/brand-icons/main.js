var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// src/main.ts
var main_exports = {};
__export(main_exports, {
  default: () => BrandIconPlugin
});
module.exports = __toCommonJS(main_exports);
var import_obsidian3 = require("obsidian");

// src/providers/provider.ts
var providers = [];
function getProvider(id) {
  return providers.find((p) => p.id === id);
}
function getDefaultProvider() {
  return providers[0];
}

// src/providers/brandfetch.ts
var VARIANT_PATH = {
  icon: "",
  logo: "/logo",
  symbol: "/symbol"
};
var brandfetch = {
  id: "brandfetch",
  name: "Brandfetch",
  supportedVariants: ["icon", "logo", "symbol"],
  defaultVariant: "icon",
  settingsFields: [
    {
      key: "clientId",
      name: "Client ID",
      description: "Your Brandfetch client ID from the developer portal.",
      placeholder: "Enter your client ID"
    }
  ],
  buildUrl(domain, variant, size, config) {
    var _a;
    const variantPath = (_a = VARIANT_PATH[variant]) != null ? _a : "";
    const params = new URLSearchParams();
    const clientId = config["brandfetch.clientId"];
    if (clientId) {
      params.set("c", clientId);
    }
    params.set("h", String(size));
    return `https://cdn.brandfetch.io/${encodeURIComponent(domain)}${variantPath}?${params.toString()}`;
  }
};
providers.push(brandfetch);

// src/editor-extension.ts
var import_view = require("@codemirror/view");
var import_obsidian = require("obsidian");

// src/brand-element.ts
function createBrandImg(doc, token, settings) {
  var _a, _b, _c;
  const provider = (_a = getProvider(settings.provider)) != null ? _a : getDefaultProvider();
  const variant = (_b = token.variant) != null ? _b : settings.defaultVariant;
  const size = (_c = token.size) != null ? _c : settings.defaultSize;
  const url = provider.buildUrl(
    token.domain,
    variant,
    size,
    settings.providerConfig
  );
  const img = doc.createElement("img");
  img.src = url;
  img.alt = `${token.domain} ${variant}`;
  img.classList.add("brand-icons-inline");
  if (token.size) {
    img.style.height = `${size}px`;
  }
  return img;
}

// src/parse.ts
var BRAND_PATTERN = /:brand:([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?:\|([a-z]+))?(?:\|(\d+))?:/g;
function findBrandSpans(text) {
  const spans = [];
  BRAND_PATTERN.lastIndex = 0;
  for (let match = BRAND_PATTERN.exec(text); match !== null; match = BRAND_PATTERN.exec(text)) {
    const token = { domain: match[1] };
    if (match[2]) {
      token.variant = match[2];
    }
    if (match[3]) {
      token.size = parseInt(match[3], 10);
    }
    spans.push({
      from: match.index,
      to: match.index + match[0].length,
      token
    });
  }
  return spans;
}

// src/editor-extension.ts
var BrandWidget = class extends import_view.WidgetType {
  constructor(token, plugin) {
    super();
    this.token = token;
    this.plugin = plugin;
  }
  toDOM() {
    return createBrandImg(activeDocument, this.token, this.plugin.settings);
  }
  eq(other) {
    return this.token.domain === other.token.domain && this.token.variant === other.token.variant && this.token.size === other.token.size;
  }
};
function buildDecorations(view, plugin) {
  const decorations = [];
  for (const { from, to } of view.visibleRanges) {
    const text = view.state.sliceDoc(from, to);
    const spans = findBrandSpans(text);
    for (const span of spans) {
      const absFrom = from + span.from;
      const absTo = from + span.to;
      const cursorHead = view.state.selection.main.head;
      if (cursorHead >= absFrom && cursorHead <= absTo) {
        continue;
      }
      decorations.push({
        from: absFrom,
        to: absTo,
        decoration: import_view.Decoration.replace({
          widget: new BrandWidget(span.token, plugin)
        })
      });
    }
  }
  return import_view.Decoration.set(
    decorations.map((d) => d.decoration.range(d.from, d.to))
  );
}
function brandIconExtension(plugin) {
  return import_view.ViewPlugin.fromClass(
    class {
      constructor(view) {
        if (view.state.field(import_obsidian.editorLivePreviewField)) {
          this.decorations = buildDecorations(view, plugin);
        } else {
          this.decorations = import_view.Decoration.none;
        }
      }
      update(update) {
        if (!update.view.state.field(import_obsidian.editorLivePreviewField)) {
          this.decorations = import_view.Decoration.none;
          return;
        }
        if (update.docChanged || update.viewportChanged || update.selectionSet) {
          this.decorations = buildDecorations(update.view, plugin);
        }
      }
    },
    { decorations: (v) => v.decorations }
  );
}

// src/post-processor.ts
function brandIconPostProcessor(settings) {
  return (el) => {
    var _a;
    const walker = el.ownerDocument.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    const replacements = [];
    let textNode = walker.nextNode();
    while (textNode) {
      const text = (_a = textNode.textContent) != null ? _a : "";
      const spans = findBrandSpans(text);
      if (spans.length > 0) {
        replacements.push({
          node: textNode,
          fragments: buildFragments(text, spans, settings, el.ownerDocument)
        });
      }
      textNode = walker.nextNode();
    }
    for (const { node, fragments } of replacements) {
      const parent = node.parentNode;
      if (!parent)
        continue;
      const span = el.ownerDocument.createElement("span");
      for (const fragment of fragments) {
        if (typeof fragment === "string") {
          span.appendChild(el.ownerDocument.createTextNode(fragment));
        } else {
          span.appendChild(fragment);
        }
      }
      parent.replaceChild(span, node);
    }
  };
}
function buildFragments(text, spans, settings, doc) {
  const fragments = [];
  let lastIndex = 0;
  for (const span of spans) {
    if (span.from > lastIndex) {
      fragments.push(text.slice(lastIndex, span.from));
    }
    fragments.push(createBrandImg(doc, span.token, settings));
    lastIndex = span.to;
  }
  if (lastIndex < text.length) {
    fragments.push(text.slice(lastIndex));
  }
  return fragments;
}

// src/settings.ts
var import_obsidian2 = require("obsidian");
var DEFAULT_SETTINGS = {
  provider: "brandfetch",
  defaultSize: 20,
  defaultVariant: "icon",
  providerConfig: {}
};
var BrandIconSettingTab = class extends import_obsidian2.PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }
  display() {
    var _a;
    const { containerEl } = this;
    containerEl.empty();
    const activeProvider = (_a = getProvider(this.plugin.settings.provider)) != null ? _a : getDefaultProvider();
    new import_obsidian2.Setting(containerEl).setName("Provider").setDesc("Which brand icon service to use.").addDropdown((dropdown) => {
      for (const p of providers) {
        dropdown.addOption(p.id, p.name);
      }
      dropdown.setValue(activeProvider.id).onChange(async (value) => {
        var _a2;
        this.plugin.settings.provider = value;
        const newProvider = (_a2 = getProvider(value)) != null ? _a2 : getDefaultProvider();
        this.plugin.settings.defaultVariant = newProvider.defaultVariant;
        await this.plugin.saveSettings();
        this.display();
      });
    });
    new import_obsidian2.Setting(containerEl).setName("Default size").setDesc("Default icon height in pixels.").addText(
      (text) => text.setPlaceholder("20").setValue(String(this.plugin.settings.defaultSize)).onChange(async (value) => {
        const parsed = parseInt(value, 10);
        if (!Number.isNaN(parsed) && parsed > 0) {
          this.plugin.settings.defaultSize = parsed;
          await this.plugin.saveSettings();
        }
      })
    );
    if (activeProvider.supportedVariants.length > 1) {
      new import_obsidian2.Setting(containerEl).setName("Default variant").setDesc("Which logo variant to use by default.").addDropdown((dropdown) => {
        for (const v of activeProvider.supportedVariants) {
          dropdown.addOption(v, v.charAt(0).toUpperCase() + v.slice(1));
        }
        dropdown.setValue(this.plugin.settings.defaultVariant).onChange(async (value) => {
          this.plugin.settings.defaultVariant = value;
          await this.plugin.saveSettings();
        });
      });
    }
    for (const field of activeProvider.settingsFields) {
      const configKey = `${activeProvider.id}.${field.key}`;
      new import_obsidian2.Setting(containerEl).setName(field.name).setDesc(field.description).addText((text) => {
        var _a2, _b;
        text.setPlaceholder((_a2 = field.placeholder) != null ? _a2 : "").setValue((_b = this.plugin.settings.providerConfig[configKey]) != null ? _b : "").onChange(async (value) => {
          this.plugin.settings.providerConfig[configKey] = value;
          await this.plugin.saveSettings();
        });
      });
    }
  }
};

// src/main.ts
var BrandIconPlugin = class extends import_obsidian3.Plugin {
  constructor() {
    super(...arguments);
    this.settings = DEFAULT_SETTINGS;
  }
  async onload() {
    await this.loadSettings();
    this.registerMarkdownPostProcessor(brandIconPostProcessor(this.settings));
    this.registerEditorExtension(brandIconExtension(this));
    this.addSettingTab(new BrandIconSettingTab(this.app, this));
  }
  async loadSettings() {
    this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
  }
  async saveSettings() {
    await this.saveData(this.settings);
  }
};

/* nosourcemap */
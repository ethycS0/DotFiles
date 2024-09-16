local base = require("plugins.configs.lspconfig")
local on_attach = base.on_attach
local capabilities = base.capabilities

local lspconfig = require("lspconfig")

lspconfig.pylsp.setup({
    on_attach = on_attach,
    capabilities = capabilities,
    cmd = { "pylsp" },
    filetypes = { "python" },
    single_file_support = true,
})

lspconfig.asm_lsp.setup({
  on_attach = on_attach,
  capabilities = capabilities,
  cmd = {"asm-lsp"},
  filetypes = {"asm", "s", "S"},
  root_dir = lspconfig.util.root_pattern(".config/asm-lsp/asm-lsp.toml"),
})

lspconfig.clangd.setup ({
  on_attach = function(client, bufnr)
    client.server_capabilities.signatureHelpProvider = false
    on_attach(client, bufnr)
  end,
  capabilities = capabilities,
  filetypes = { "c", "cpp", "objc", "objcpp", "cuda", "proto" },
  cmd = { "clangd" },
  root_dir = lspconfig.util.root_pattern(
          '.clangd',
          '.clang-tidy',
          '.clang-format',
          'compile_commands.json',
          'compile_flags.txt',
          'configure.ac',
          '.git'
        ),
})

require'lspconfig'.marksman.setup({
    on_attach = on_attach,
    capabilities = capabilities,
    cmd = { "marksman", "server" },
    filetypes = { "markdown", "markdown.mdx" },
    root_dir = lspconfig.util.root_pattern(".git", ".marksman.toml"),
    single_file_support = true,
})

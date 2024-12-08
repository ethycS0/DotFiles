---@type ChadrcConfig
local M = {}
M.plugins = 'custom.plugins'
M.ui = {
        theme = 'ayu_dark',
        hl_override = require "custom.theme"
}
M.mappings = require("custom.mappings")
return M

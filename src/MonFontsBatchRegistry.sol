// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract MonFontsBatchRegistry {
    struct FontMeta {
        string name;
        string ipfsHash;
        address creator;
    }

    event BatchRegistered(uint256 count, address creator);

    function registerBatch(string[] memory _names, string[] memory _ipfsHashes) public {
        require(_names.length == _ipfsHashes.length, "Data mismatch");
        require(_names.length <= 100, "Max batch size 100");

        for (uint256 i = 0; i < _names.length; i++) {
            // Logic to emit event or store mapping
        }
        emit BatchRegistered(_names.length, msg.sender);
    }
}

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract MonFontsRegistry {
    struct FontMeta {
        string name;
        string ipfsHash; // Link to the actual .ttf file on IPFS
        address creator;
        uint256 timestamp;
    }

    mapping(uint256 => FontMeta) public fonts;
    uint256 public fontCount;

    event FontSynthesized(uint256 indexed id, string name, address creator);

    function registerFont(string memory _name, string memory _ipfsHash) public {
        fontCount++;
        fonts[fontCount] = FontMeta(_name, _ipfsHash, msg.sender, block.timestamp);
        emit FontSynthesized(fontCount, _name, msg.sender);
    }
}
